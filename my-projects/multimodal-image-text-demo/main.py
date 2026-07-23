from pathlib import Path

import torch
from PIL import Image
from transformers import CLIPProcessor, CLIPModel


def load_clip_model():
    model_name = "openai/clip-vit-base-patch32"

    model = CLIPModel.from_pretrained(model_name)
    processor = CLIPProcessor.from_pretrained(model_name)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = model.to(device)
    model.eval()

    return model, processor, device


def match_image_with_text(image_path, candidate_texts, model, processor, device):
    image = Image.open(image_path).convert("RGB")

    inputs = processor(
        text=candidate_texts,
        images=image,
        return_tensors="pt",
        padding=True,
    )

    inputs = {
        key: value.to(device)
        for key, value in inputs.items()
    }

    with torch.no_grad():
        outputs = model(**inputs)

    logits_per_image = outputs.logits_per_image
    probs = logits_per_image.softmax(dim=1)[0]

    results = []

    for text, prob in zip(candidate_texts, probs):
        results.append({
            "text": text,
            "score": prob.item(),
        })

    results = sorted(
        results,
        key=lambda item: item["score"],
        reverse=True,
    )

    return results


def print_results(image_path, results):
    print("=" * 60)
    print(f"Image: {image_path}")
    print("-" * 60)

    for index, item in enumerate(results, start=1):
        print(f"{index}. {item['text']}")
        print(f"   score: {item['score']:.4f}")

    print("-" * 60)
    print(f"Best match: {results[0]['text']}")
    print("=" * 60)


def main():
    model, processor, device = load_clip_model()

    candidate_texts = [
        "a handwritten digit zero",
        "a handwritten digit one",
        "a handwritten digit two",
        "a handwritten digit three",
        "a handwritten digit four",
        "a handwritten digit five",
        "a handwritten digit six",
        "a handwritten digit seven",
        "a handwritten digit eight",
        "a handwritten digit nine",
        "a cat",
        "a car",
        "a dog",
    ]

    image_paths = [
        Path("test_images/test_digit_3.png"),
        Path("test_images/test_digit_7.png"),
    ]

    for image_path in image_paths:
        results = match_image_with_text(
            image_path=image_path,
            candidate_texts=candidate_texts,
            model=model,
            processor=processor,
            device=device,
        )

        print_results(image_path, results)


if __name__ == "__main__":
    main()