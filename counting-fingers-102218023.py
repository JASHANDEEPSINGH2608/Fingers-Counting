import os
import csv
from PIL import Image
from landingai.predict import Predictor

endpoint_id = "1ef2e652-710a-42ef-9236-7f92dd73f3ae"
api_key = "land_sk_7VVG8HeQUOjnENhi5ZoE6yL0H8sl4IURmmwvj7Zh6l620u1sGk"


image_folder = "C:/Users/jasha/OneDrive/Desktop/Fingers-Images"
output_csv = "output_results.csv"


predictor = Predictor(endpoint_id, api_key=api_key)


results = []


for image_name in os.listdir(image_folder):
    if image_name.lower().endswith(('.png', '.jpg', '.jpeg')):

        image_path = os.path.join(image_folder, image_name)
        image = Image.open(image_path)


        predictions = predictor.predict(image)


        if predictions and isinstance(predictions, list):
            result = predictions[0].label_name  # Adjust this field as necessary
        else:
            result = "No prediction found"


        results.append([image_name, result])


with open(output_csv, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Image Name", "Prediction Result"])
    writer.writerows(results)

print(f"Results saved to {output_csv}")
