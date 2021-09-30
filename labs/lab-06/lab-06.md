# Lab 06: Query matching with FastText and Virtex


## Launch a FastText service using the Virtex library in Python
The purpose of this lab is to expose you to a few things:

(a) The [FastText](https://fasttext.cc/docs/en/python-module.html) library in Python, which is a language modeling and text classification framework

(b) The idea that NLP systems typically take on the form of microservices, wherein specific functions, such as computing embeddings, or computing similar words, are performed in isolation and accessed through HTTP requests (or other protocols such as gRPC).

(c) The [Advanced Rest Client](https://install.advancedrestclient.com/install) (ARC), which allows you to make HTTP requests containing data (such as JSON) to an HTTP endpoint.

(d) The [Virtex](https://pypi.org/project/virtex/) library, which provides a convenient way to expose your machine learning computation as a service over HTTP without having to write any networking code (see `query_matching_demo.py`, `query_matching_demo.sh`).


## Task I (20 pts)

1. Download a pretrained FastText model [here](https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.en.300.bin.gz)

2. Launch the FastText query matching service by running the following command from the terminal from within the `labs/lab-06/` directory:

    $ ./query_matching_demo.sh

3. Open your Advanced Rest Client application (you need to download it first)

    a. Enter `http://0.0.0.0:580` into the Request URL bar
    
    b. In the Body content type field choose `application/json`

    c. Click the body tab and enter `{"data": ["dogs", "bakery", "hose", "florida", "supreme"]}`

    d. Explore FastText by changing the words and looking at the matches. Paste of a few of them below:

    ``` 
    # Query results go here
    ``` 
