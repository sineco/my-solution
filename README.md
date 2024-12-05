# Chat Message Event Detection Project

## Overview
This project connects to a chat application, extracts relevant conversations, and monitors messages for potential calendar events. The primary goal is to classify messages into categories related to scheduling and save them as JSON files for further use.

### Key Features:
1. **Chat Connection:** Connects to a chat application to monitor message streams.
2. **Event Detection:** Detects and categorizes messages that can be converted into calendar events.
3. **JSON Storage:** Saves detected events in individual JSON files for future processing.
4. **Custom NER Model:** Uses a Named Entity Recognition (NER) model to classify messages.
5. **Extensibility:** Designed to integrate with calendar services in the future.

## Event Detection
The project uses a NER-based model to classify messages into the following categories:

- **`O`**: Outside any named entity.
- **`B-PLATFORM`**: Beginning of a platform-related entity.
- **`I-PLATFORM`**: Inside a platform-related entity.
- **`B-TIME`**: Beginning of a time-related entity.
- **`I-TIME`**: Inside a time-related entity.
- **`B-DATE`**: Beginning of a date-related entity.
- **`I-DATE`**: Inside a date-related entity.

### Model Selection
- **NER Model:**
  - [google-bert/bert-base-cased](https://huggingface.co/google-bert/bert-base-cased)

The project uses BERT-base-cased as the primary model. For fine-tuning, the Hugging Face `Trainer` API (PyTorch-based) is used.

## Data Preparation
- **Custom Dataset:** A manually annotated dataset is created for training.
- **Padding:** Data is padded by batch to optimize processing speed.
- **Schema Design:** Follows guidelines for schema creation, such as [Microsoft Learn’s guide](https://learn.microsoft.com/en-us/azure/ai-services/).

## JSON File Format
Detected events are saved in the format:
```
event_00001.json
event_00002.json
event_00003.json
...
```
Each file contains structured information about the detected event.

## Event Detection Logic
- **Message Grouping:** Groups messages by time window or context to identify related messages.
- **NER Classification:** Applies the selected model to identify key entities and classify message intent.

## Assumptions
- The system does not create actual calendar invites.
- Only messages related to booking meetings are considered relevant.
- High availability for the service is assumed.

## Future Directions
- **Service Integration:** Extend functionality to create calendar invites.
- **Improved Detection:** Fine-tune the model for better accuracy with additional data.
- **High-Performance Storage:** Evaluate message storage strategies for relevant and non-relevant messages.

## Getting Started
### Prerequisites
- Python 3.8+
- Libraries: Hugging Face Transformers, PyTorch.

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/sineco/my-solution.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Usage
1. Start the service to connect to the chat application.
2. Monitor the message stream.
3. Train the NER model on a custom dataset.
4. Save detected events as JSON files.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request with your proposed changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

For questions or feedback, please contact [project_owner_email@example.com](mailto:project_owner_email@example.com).

