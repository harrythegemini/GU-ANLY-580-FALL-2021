# Lab-11: Speech Recognition

This Lab provides a brief introduction to open source speech recognition tools from the [Huggingface library](https://huggingface.co/transformers/) and from [NVIDIA's NeMO toolkit](https://github.com/NVIDIA/NeMo). The graded portion of this lab can be found below. In it we will transcribe and audio recording of our voice using the [Wave2Vec2.0 model](https://huggingface.co/transformers/model_doc/wav2vec2.html), and then evaluate the quality of the transcription using [word](https://huggingface.co/metrics/wer) and [character](https://huggingface.co/metrics/cer) error rates. If you'd like to dig deeper, there is a tutorial (`lab-11.ipynb`) from NVIDIA NeMo that will give you an idea of what goes into online voice recognition, which requires us to stream an audio signal directly from a microphone into the model running in your python process. This Jupyter notebook will not be graded.

## Speech recognition with Wave2Vec2.0


### Task I (20 pts)

Take a look at `asr.py`. In it you'll find four different modes: record, play, transcribe, evaluate. To get started, issue the following command:

    $ python asr.py record myvoice.wav 30
    
Following the prompt from the terminal, read aloud the text in `ground-truth.txt`. To make sure your voice was recorded properly, run the script in *play* mode:

    $ python asr.py play myvoice.wav 30
    
Next, we're going to transcribe this audio file using the Wave2Vec2.0 base model from Huggingface. Issue the following command:

    $ python asr.py transcribe myvoice.wav
    
Finally, we need to evaluate the quality of our model's transcription by measuring the word error rate (WER) and character error rate (CER). Issue the following command:

    $ python asr.py evaluate myvoice_transcription.txt ground-truth.txt

This command will produce a `results.json` file containing the WER and CER metrics metrics. Submit the resultant audio file, transcription, and results files to your github repo.


### Task II (10 pts)

1. How would you grade the models transcriptions of your voice (without considering WER)?

2. Why is the character level error rate lower than at the word level?

3. Are the models errors primarily on the word level, or is it missing phonetic sounds all together? Given this assessment, if you had to improve this model, would you focus primarily on the acoustic model or the language model?


