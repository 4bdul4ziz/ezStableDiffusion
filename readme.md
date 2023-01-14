# ezStableDiffusion

ezStableDiffusion is a simple graphical user interface (GUI) built with tkinter and customtkinter, which allows users to easily generate images using the StableDiffusion pipeline. 

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.6 or later
- `tkinter` and `customtkinter` (can be installed via pip)
- `Pillow` (can be installed via pip)
- `torch` and `torchvision` (can be installed via pip)
- `authtoken` (should be provided by the developer)
- `diffusers` (should be provided by the developer)

### Installation

1. Clone the repository.
2. Install the prerequisites via pip by running `pip install -r requirements.txt`
3. Set the environment variable `cache_dir` to the directory where the models will be stored. 
4. Run the script `main.py`

## Usage

1. Run the script `main.py`
2. Type in the prompt the text you want to use as guidance for the image generation.
3. Click on the "Generate" button.
4. The generated image will be displayed and also saved as "generated.png" in the working directory.

## Built With

- [tkinter](https://docs.python.org/3/library/tkinter.html) - Python's standard GUI package
- [customtkinter](https://github.com/jackwilsdon/customtkinter) - A wrapper for tkinter to make it easier to use
- [Pillow](https://pillow.readthedocs.io/en/stable/) - A python imaging library
- [torch](https://pytorch.org/) - PyTorch is an open source machine learning library
- [diffusers](https://github.com/google-research/google-research/tree/main/diffusers) - A library for image generation

## Authors

- **Developer** - *Initial work* - [Abdul Aziz](https://github.com/4bdul4ziz)

## Acknowledgments

- The StableDiffusion pipeline is based on the paper ["Stable Diffusion Generative Models"](https://arxiv.org/abs/2101.09386) by Google Research
- The customtkinter library is based on the work of [Jack Wilsdon](https://github.com/jackwilsdon)
