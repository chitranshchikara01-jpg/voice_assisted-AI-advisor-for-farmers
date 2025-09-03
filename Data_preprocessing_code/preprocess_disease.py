import os
import cv2
import numpy as np

input_folder = "C:\\Users\\guddu\\OneDrive\\Desktop\\Internship project\\data\\PlantVillage"
processed_array_folder = "processed_data/arrays"   # numpy arrays ke liye
processed_image_folder = "processed_data/images"   # jpg/png ke liye

# Folders create kar do agar nahi hai
os.makedirs(processed_array_folder, exist_ok=True)
os.makedirs(processed_image_folder, exist_ok=True)

IMG_SIZE = 128  # resize size

count = 0
for root, dirs, files in os.walk(input_folder):
    for file in files:
        if file.endswith(".jpg") or file.endswith(".png"):
            img_path = os.path.join(root, file)
            img = cv2.imread(img_path)

            if img is not None:
                # Resize + Normalize
                img_resized = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                img_normalized = img_resized / 255.0

                # ---- (1) Numpy array save ----
                np.save(os.path.join(processed_array_folder, f"image_{count}.npy"), img_normalized)

                # ---- (2) Image file save (taaki open kar sako) ----
                cv2.imwrite(os.path.join(processed_image_folder, f"image_{count}.jpg"), img_resized)

                count += 1

print(f"✅ Preprocessing complete! {count} images processed.")
print("👉 Arrays saved in:", processed_array_folder)
print("👉 Images saved in:", processed_image_folder)

        
     
