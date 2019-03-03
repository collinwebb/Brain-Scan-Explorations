## Brain Scan Explorations

### Running the code

#### Setup

To install run:

First make sure you have the latest version of Anaconda (this was done with version 4.6.7), then run the following:

```
conda env create -f environment.yml
conda activate mne
pip install --upgrade "pyqt5>=5.10" # on mac only
```

When going back to the project with Anaconda already set up, just use:

```
conda activate mne
```

#### Run

```
python exploations.py
```

#### deactivate

To get back to base conda environment:
```
conda deactivate
```

### Background

I got an original Muse headband (v2, 2016) and have used it some for my mindfulness practice. Most of my mindfulness practice has been attempts to be present in the moment to moment of every day life. There is a human bias called the [context effect and mood-congruent memory bias](https://en.wikipedia.org/wiki/Cue-dependent_forgetting) where we can't remember things when we are in a different context, or it is easier to remember something when it is congruent with our current mood. So if we do all our mindfulness practice sitting down and being quite, we won't remember to pay attention to ourselves and our surroundings when something else is happening in life. This is at least true for me, so I practice all the time, as often as I can remember in all cirumstances.

I'm also a searcher after truth, and some of the best ways we humans have found to understand something is by building machines that can measure reality. So I got one and am going to play around with reading some data I gather and see what I can find. I can make all sorts of hypotheses and test them, or I can just explore the data and try a lot of different strange things until I run across something interesting. I will probably do both. \^\_\^

### Further Steps

I'm planning to explore what scripting languages I can use to explore the different aspects of brain scans I take. I suspect I will end up using Python for this. Then I'm going to start making a few simple scripts to look at what is going on with my brain when I'm doing different things. These scripts may turn into a generalized program to explore brain activity.

I also need to keep taking more scans and collecting more data. I will start with me, but then I will move onto scans from other people and see if there is anything I can learn about how neural oscillations work.

I'm going to start with [mne-python](https://github.com/mne-tools/mne-python). I tried looking at some simpler tools, but they didn't have good enough documentation to follow easily or had issues installing dependencies. mne-python also uses conda!! So, I don't have to deal with package issues.


### Todo

- script installation
