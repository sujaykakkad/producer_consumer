# Producer-Consumer Application

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Overview

This is a Python-based implementation of the Producer-Consumer problem using threading and semaphores. The application simulates producers publishing messages to topics and consumers subscribing to topics to consume messages.

## Features

- **Producers**: Publish messages to specific topics.
- **Consumers**: Subscribe to topics and consume messages.
- **Topics**: Manage messages with a fixed capacity using semaphores.
- **Threading**: Uses `ThreadPoolExecutor` for concurrent execution of producers and consumers.

## Prerequisites

- Python 3.8.2 or higher

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd producer_consumer
   ```

2. Install required dependencies (if any). This project does not currently use external libraries beyond Python's standard library.

## Usage

1. Initialize the application by running the main script:
   ```sh
   python3 src/index.py
   ```

2. The script will:
   - Create topics (`topic1`, `topic2`).
   - Add producers and consumers.
   - Simulate message publishing and consumption.

## Code Structure

```
.gitignore
README.md
src/
    consumer.py       # Consumer class implementation
    index.py          # Entry point of the application
    message_queue.py  # MessageQueue class to manage topics
    producer.py       # Producer class implementation
    topic.py          # Topic class to manage messages
    util.py           # Utility functions (ThreadPoolExecutor initialization)
```

### Key Components

- **Producer**: Defined in [`src/producer.py`](src/producer.py), the `Producer` class publishes messages to topics asynchronously.
- **Consumer**: Defined in [`src/consumer.py`](src/consumer.py), the `Consumer` class subscribes to topics and listens for messages.
- **Topic**: Defined in [`src/topic.py`](src/topic.py), the `Topic` class manages messages using a queue and semaphores.
- **MessageQueue**: Defined in [`src/message_queue.py`](src/message_queue.py), the `MessageQueue` class manages multiple topics.
- **Utilities**: Defined in [`src/util.py`](src/util.py), initializes a `ThreadPoolExecutor` for concurrent execution.

### How Topics Handle Messages

The `Topic` class uses Python's `Semaphore` to manage concurrent access to its message queue. Here's how it works:

- **Semaphores**:
  - `mutex`: Ensures mutual exclusion when accessing the message queue.
  - `empty`: Tracks the number of empty slots in the queue (initialized to the topic's capacity).
  - `full`: Tracks the number of messages available in the queue (initialized to 0).

- **Message Addition**:
  - A producer acquires the `empty` semaphore before adding a message, ensuring there is space in the queue.
  - The `mutex` semaphore is then acquired to safely add the message to the queue.
  - After adding the message, the `mutex` is released, and the `full` semaphore is incremented to signal that a new message is available.

- **Message Removal**:
  - A consumer acquires the `full` semaphore before removing a message, ensuring there is at least one message in the queue.
  - The `mutex` semaphore is then acquired to safely remove the message from the queue.
  - After removing the message, the `mutex` is released, and the `empty` semaphore is incremented to signal that a slot is now available.

This mechanism ensures thread-safe operations and prevents race conditions while managing the queue.

## Example Output

When you run the application, you will see output similar to the following:

```
Published Message Message 1 to topic topic1
Published Message Message 2 to topic topic1
1 received Message 1
2 received Message 2
Published Message Message 3 to topic topic1
3 received Message 3
Published Message Message 4 to topic topic2
Published Message Message 5 to topic topic2
4 received Message 4
5 received Message 5
```

## Notes

- The `CAPACITY_PER_TOPIC` in [`src/topic.py`](src/topic.py) is set to 10. You can modify this value to change the maximum number of messages a topic can hold.
- The `ThreadPoolExecutor` in [`src/util.py`](src/util.py) is configured with a maximum of 10 workers. Adjust this based on your requirements.

## Contributing

Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License.