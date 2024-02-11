# Postmanner

**⚠️ This extension is currently under development and may have limited functionality. Use with caution. ⚠️**

Postmanner is an extension that converts HTTP requests sent through Burp Suite into a Postman collection.

## Features

- Converts all requests under Proxy -> HTTP History tab into a collection.
- Allows customizing the Collection Name, which will be displayed on Postman.
- Enables creating a collection specific to a domain by selecting the domains where requests were made in the History tab.

## Filter Options

Before creating a collection, you can filter requests to convert only the desired ones.

## Usage

1. Open Burp Suite and navigate to the Postmanner tab.
2. Configure the desired filters or leave them empty to convert all requests.
3. Click on "Save" to generate the collection.

## Configuration

### Collection Name

Set a custom name for the collection that will be displayed in Postman.

### Domain List

Create collections specific to certain domains by selecting the domains in the History tab.

Feel free to contribute or report issues!

![postmanner](https://github.com/yasin-olgun/postmanner/assets/50578544/9d82960f-40f4-4d73-8465-8ed5884f022a)


## License

This project is licensed under the [MIT License](LICENSE).


