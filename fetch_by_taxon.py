import os
import requests
import argparse

def get_taxon_name(taxon_path):
    taxon_id = taxon_path.strip("/").split("/")[-1]
    response = requests.get(f"https://api.inaturalist.org/v1/taxa/{taxon_id}")
    if response.status_code != 200:
        raise ValueError(f"Could not fetch taxon with ID {taxon_id}")
    data = response.json()
    if not data.get("results"):
        raise ValueError(f"No taxon found for ID {taxon_id}")
    return data["results"][0]["name"]

def fetch_observations(taxon_name, count):
    url = "https://api.inaturalist.org/v1/observations"
    params = {
        "taxon_name": taxon_name,
        "per_page": min(count, 200),
        "order_by": "observed_on",
        "order": "desc",
        "photos": "true"
    }

    observations = []
    page = 1
    while len(observations) < count:
        params["page"] = page
        response = requests.get(url, params=params)
        data = response.json()
        results = data.get("results", [])
        if not results:
            break
        observations.extend(results)
        if len(results) < params["per_page"]:
            break
        page += 1

    return observations[:count]

def download_images(observations, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for idx, obs in enumerate(observations):
        photos = obs.get("photos", [])
        if not photos:
            continue

        image_url = photos[0].get("url", "").replace("square", "original")
        try:
            image_data = requests.get(image_url).content
            filename = f"image_{idx+1:03}.jpg"
            with open(os.path.join(output_dir, filename), "wb") as f:
                f.write(image_data)
            print(f"Downloaded {filename}")
        except Exception as e:
            print(f"Failed to download image {idx+1}: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--taxon", type=str, required=True, help="Taxon path, e.g. /taxa/68328")
    parser.add_argument("--count", type=int, default=100, help="Number of observations to fetch (max 300 recommended)")
    parser.add_argument("--output", type=str, default="output_images", help="Folder to save downloaded images")
    args = parser.parse_args()

    try:
        taxon_name = get_taxon_name(args.taxon)
        print(f"Resolved taxon ID {args.taxon} to: {taxon_name}")
    except ValueError as e:
        print(f"Error: {e}")
        return

    observations = fetch_observations(taxon_name, args.count)
    download_images(observations, args.output)

if __name__ == "__main__":
    main()