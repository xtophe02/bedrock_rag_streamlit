# Venthone HR Q & A with RAG (Retrieval-Augmented Generation)

This project implements a Retrieval-Augmented Generation (RAG) system to answer questions related to HR documents. The system uses advanced natural language processing techniques to retrieve relevant information from PDF documents and generate accurate responses.

## Features

- **Document Processing**: Load and split PDF documents for efficient retrieval.
- **Vector Storage**: Use FAISS for efficient similarity search on document embeddings.
- **Language Model**: Generate responses using the AWS Bedrock LLM.
- **User Interface**: An interactive UI built with Streamlit for querying the documents.

## Installation

### Prerequisites

- Python 3.7 or higher
- Required Python packages (listed below)

### Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/venthone-rag-qa.git
   cd venthone-rag-qa
   ```

2. **Install the required packages**:

   You can install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

   If a `requirements.txt` file is not provided, you may manually install the necessary packages:

   ```bash
   pip install streamlit langchain langchain_community pdfplumber faiss-cpu
   ```

3. **Prepare your documents**:

   Place your PDF documents in the `data/` directory or specify the path in `rag_backend.py`.

## Usage

1. **Start the Streamlit application**:

   Run the Streamlit application with the following command:

   ```bash
   streamlit run rag_frontend.py
   ```

2. **Interact with the UI**:

   - Open the application in your web browser.
   - Enter your query in the text area and click "Ask to your docs".
   - The system will process your query and return relevant information from the HR documents.

## File Structure

- `rag_backend.py`: Contains the backend logic for document processing and response generation.
- `rag_frontend.py`: Contains the frontend logic using Streamlit to create an interactive user interface.

## Customization

- **UI Customization**: You can modify the title, button labels, and other UI elements in `rag_frontend.py`.
- **Document and Index Settings**: Adjust document loading and indexing settings in `rag_backend.py` according to your needs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

This project utilizes the `langchain` library for document processing and AWS's Bedrock LLM for response generation. The frontend is built using Streamlit.
