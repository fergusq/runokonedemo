# Runokonedemo

## Riippuvuudet

Riippuvuudet voi asentaa pipillä seuraavasti:

```sh
pip install -r requirements.txt
```

Lisäksi kielimalli tulee asettaa samaan kansioon. 
Demo tukee periaatteessa mitä vain kielimalleja, mutta siihen on oletuksena konfiguroitu Ahma 3B Instruct -malli.
Sen voi ladata [HuggingFacesta](https://huggingface.co/mradermacher/Ahma-3B-Instruct-GGUF/resolve/main/Ahma-3B-Instruct.Q6_K.gguf?download=true).

## Käyttö

Demo käynnistetään seuraavasti:

Käynnistä root-käyttäjänä (sudolla) pipe.sh:

```sh
sudo ./pip.sh
```

Käynnistä toisessa ikkunassa itse ohjelma tavallisena käyttäjänä:

```sh
./run.sh
```

## Muuta

[Cool-retro-term-pääte-emulaattorilla](https://github.com/Swordfish90/cool-retro-term) saa demoon tunnelmallisuutta.
