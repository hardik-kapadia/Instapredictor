from instagram_data import InstagramData


def read_names_from_files(filename: str = "instagram handle list.txt"):

    names = set()

    count = 0

    with open(filename, "r") as f:

        for line in f:
            if count >= 10:
                break

            count += 1
            names.add(line.strip())

    return names


if __name__ == "__main__":
    igd = InstagramData()

    profiles = read_names_from_files()

    # profiles = ['shikhatalsania','zomato']

    non_existant = []
    errors = []

    for profile in profiles:
        try:
            igd.download_ig_profile(profile)
        except ValueError as e:
            errors.append(profile)
            print(f" getting error for profile {profile} -> {e}")

    print(f"errors: {errors}")
