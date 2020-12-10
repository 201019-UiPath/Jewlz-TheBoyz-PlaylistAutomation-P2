# Attachment Performer

## Description

This project utilizes the RE Framework to ensure robust transaction processing. The process will collect queue data items in the form of attachments and perform operations based on the attachment.

## How to use

1. Open data/config.xlsx file
2. change the value of the "OrchestratorQueueName" to the name of your desired queue that resides in orchestrator
3. Whenever accessing queue items call this in process.xaml: in_TransactionItem.SpecificContent("nameOfDataInQueue")
* As long as the string here matches the same name as the string when the data was put into the queue, the attachment should be returned.
