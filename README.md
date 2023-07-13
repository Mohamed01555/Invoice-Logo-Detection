# Invoice-Logo-Detection

    - This project is a deep learning model that detects company logos from different invoices.The model is designed to extract logos from scanned or digital invoices and classify them into different categories based on the company they represent. The model is trained to detect certain logos . You can find them in logos directory.

# Description

    Invoice Logo Detector is a machine learning-based solution that can help businesses automate their invoice processing workflows. By automatically detecting and extracting logos from invoices, the system can save time and reduce errors associated with manual data entry.

    Because of lack of invoices dataset , I made a syntetic dataset by putting logos in random sizes in random places in invoice-like documents.

    Invoces-like dataset can be found here : Dataset

    Trained model can be found here : Model

    The model is trained using a dataset of company logos from different industries and regions. It uses a combination of convolutional neural networks (CNNs) and transfer learning , specifically , I used YOLOv8 to achieve high accuracy and robustness.

    The system is designed to work with both scanned and digital invoices, and can be easily integrated into existing invoice processing pipelines.

Getting Started

To use the Invoice Logo Detector, you'll need to follow these steps:

    Clone the repository to your local machine.
    Install the required dependencies and libraries using pip install -r requirements.txt.
    Run the train.py script to train the model on your own dataset, or use the pre-trained weights provided in the models directory.
    Run the detect.py script to detect logos from new invoices.

Usage

To use the Invoice Logo Detector, simply run the detect.py script and provide the path to the invoice file as an argument. The system will automatically detect and extract logos from the invoice and output the results in the specified format.

For example, to detect logos from an invoice file named example_invoice.pdf and output the results as a CSV file, run:

python detect.py --input example_invoice.pdf --output example_results.csv --format csv

Contributing

If you want to contribute to the Invoice Logo Detector project, please fork the repo and edit.
Support

If you have any questions or run into any issues with the Invoice Logo Detector, please create a new issue on the GitHub repository.
Acknowledgments

    This project was inspired by the need to automate invoice processing workflows and reduce errors associated with manual data entry. It uses the power of machine learning and deep learning to achieve high accuracy and efficiency.
    Thank to Computer vision engineer yo

    utube channel
