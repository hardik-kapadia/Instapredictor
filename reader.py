import instaloader
import os
import numpy as np
import cv2

from sentiment import SentimentAnalyser

se = SentimentAnalyser()

L = instaloader.Instaloader()


# def read_data(folder="Data"):

#     images = []
#     numeric = []
#     output = []

#     count = 0


#     for inner_folder in os.listdir(folder):
#         for filename in os.listdir(folder + "/" + inner_folder):

#             if count >= 10:
#                 break

#             count += 1

#             if filename.endswith(".json"):
#                 post_node = instaloader.structures.load_structure_from_file(
#                     L.context, os.path.join(folder, inner_folder, filename)
#                 )

#                 post_likes = post_node.likes
#                 post_comments = post_node.comments

#                 profile_followers = post_node.owner_profile.followers

#                 output.append(
#                     np.array(
#                         [
#                             post_likes / profile_followers,
#                             post_comments / profile_followers,
#                         ]
#                     )
#                 )

#                 post_caption = post_node.caption

#                 score = se.get_score(post_caption)["compound"]
#                 numeric.append(score)

#                 continue

#             img = cv2.imread(os.path.join(folder, inner_folder, filename))

#             if img is not None:
#                 imgf = cv2.resize(img, (256, 256))
#                 print(f"{img.shape} -> {imgf.shape}")
#                 images.append(imgf)

#     img_arr = np.array(images)
#     numeric_arr = np.array(numeric)
#     output_arr = np.array(output)

#     return (img_arr, numeric_arr, output_arr)


def read_data(folder="Data", metadata_ext=".json.xz"):

    images = []
    numeric = []
    output = []

    for inner_folder in os.listdir(folder):

        files_in_folder = os.listdir(folder + "/" + inner_folder)
        
        image_files = 0

        for files in files_in_folder:
            if (
                files.endswith(".png")
                or files.endswith(".jpg")
                or files.endswith(".jpeg")
            ):
                image_files += 1
        print(f"images: {image_files}")

        for filename in os.listdir(folder + "/" + inner_folder):

            if filename.endswith(metadata_ext):
                
                post_node = instaloader.structures.load_structure_from_file(
                    L.context, os.path.join(folder, inner_folder, filename)
                )

                post_likes = post_node.likes
                post_comments = post_node.comments

                profile_followers = post_node.owner_profile.followers

                post_caption = post_node.caption

                score = se.get_score(post_caption)["compound"]

                for _ in range(image_files):
                    output.append(
                        np.array(
                            [
                                post_likes / profile_followers,
                                post_comments / profile_followers,
                            ]
                        )
                    )

                    numeric.append(score)

                continue

            img = cv2.imread(os.path.join(folder, inner_folder, filename))

            if img is not None:
                imgf = cv2.resize(img, (256, 256))
                # print(f"{img.shape} -> {imgf.shape}")
                images.append(imgf)

    img_arr = np.array(images)
    numeric_arr = np.array(numeric)
    output_arr = np.array(output)

    return (img_arr, numeric_arr, output_arr)


if __name__ == "__main__":

    data = read_data(metadata_ext=".json")

    img = data[0]
    num = data[1]
    op = data[2]

    print(img[1])
    print(num)
    print(op)

    print(img.shape)

    print(num.shape)

    print(op.shape)
