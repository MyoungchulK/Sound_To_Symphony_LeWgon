import pandas as pd
import numpy as np
import collections
import pretty_midi
import glob
import tensorflow as tf

def midi_to_notes(midi_file: str) -> pd.DataFrame:
    """ midi to note conversion """

    ## extract basic
    pm = pretty_midi.PrettyMIDI(midi_file)
    instrument = pm.instruments[0]
    notes = collections.defaultdict(list)

    ## Sort the notes by start time
    sorted_notes = sorted(instrument.notes, key=lambda note: note.start)
    prev_start = sorted_notes[0].start

    for note in sorted_notes:
        start = note.start
        end = note.end
        notes['pitch'].append(note.pitch)
        notes['start'].append(start)
        notes['end'].append(end)
        notes['step'].append(start - prev_start)
        notes['duration'].append(end - start)
        prev_start = start

    return pd.DataFrame({name: np.array(value) for name, value in notes.items()})

def notes_to_midi(
    notes: pd.DataFrame,
    out_file: str,
    instrument_name: str,
    velocity: int = 100,  # note loudness
    ) -> pretty_midi.PrettyMIDI:
    """ converts the generated note to midi """ 

    ## set basic info for midi
    pm = pretty_midi.PrettyMIDI()
    instrument = pretty_midi.Instrument(
        program=pretty_midi.instrument_name_to_program(
            instrument_name))

    ## conversion
    prev_start = 0
    for i, note in notes.iterrows():
        ## conditioning to not over the range
        pitch = max(0, min(127, int(note['pitch'])))
        velocity = max(0, min(127, velocity))

        ## store in midi
        start = float(prev_start + note['step'])
        end = float(start + note['duration'])
        note = pretty_midi.Note(
            velocity=velocity,
            pitch=pitch,
            start=start,
            end=end,
        )
        instrument.notes.append(note)
        prev_start = start

    pm.instruments.append(instrument)
    pm.write(out_file)
    return pm

def process_data(self, filenames,
                      num_files = 5,
                      vocab_size = 128,                     
                      ):
     """ preprocess the test data. Not made by me... """
     
    ## list for generated note
    all_notes = []
    n_notes = len(all_notes)
    train_notes = np.stack([all_notes[key] for key in se     lf.key_order], axis=1)
    notes_ds = tf.data.Dataset.from_tensor_slices(train_     notes)
    notes_ds.element_spec

    batch_size = 64
    buffer_size = n_notes - self.seq_length  # the numbe     r of items in the dataset\
    seq_ds = self._create_sequences(notes_ds, self.seq_l     ength, vocab_size)
    seq_ds.element_spec

    train_ds = (seq_ds
                .shuffle(buffer_size)
                .batch(batch_size, drop_remainder=True)
                .cache()
                .prefetch(tf.data.experimental.AUTOTUNE))
 
         print(' --- Training Data Ready --- ')
         return train_ds
     

if __name__ == "__main__":
    data_dir = '/Users/juan-garassino/Code/le-wagon/symphony/data/maestro-v2.0.0'
    filenames = glob.glob(str(f'{data_dir}/**/*.mid*'))
    print('Number of files:', len(filenames))
    sample_file = filenames[1]
    raw_notes = midi_to_notes(sample_file)
    raw_notes.head()
