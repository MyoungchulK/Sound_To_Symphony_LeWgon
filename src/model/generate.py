import tensorflow as tf
import numpy as np

def predict_next_note(
    notes: np.ndarray,
    model: tf.keras.Model,
    temperature: float = 1.0) -> tuple[int, float, float]:
  """Generates a note as a tuple of (pitch, step, duration), using a trained sequence model."""

  assert temperature > 0

  # Add batch dimension
  inputs = tf.expand_dims(notes, 0)

  predictions = model.predict(inputs)
  pitch_logits = predictions['pitch']
  step = predictions['step']
  duration = predictions['duration']

  pitch_logits /= temperature
  pitch = tf.random.categorical(pitch_logits, num_samples=1)
  pitch = tf.squeeze(pitch, axis=-1)
  duration = tf.squeeze(duration, axis=-1)
  step = tf.squeeze(step, axis=-1)

  # `step` and `duration` values should be non-negative
  step = tf.maximum(0, step)
  duration = tf.maximum(0, duration)

  return int(pitch), float(step), float(duration)

def generate_notes_from_midi_file(self, sample_file, key     ='C_phrygian_major', seq_length=25 ,vocab_size = 128, temper     ature = 2.0, num_predictions = 120):
    """ save as midi"""
    
    raw_notes = midi_to_notes(sample_file)
    sample_notes = np.stack([raw_notes[key] for key in s     elf.key_order], axis=1)

    # The initial sequence of notes; pitch is normalized      similar to training
    input_notes = (sample_notes[:seq_length] / np.array([vocab_size     , 1, 1]))

    generated_notes = []
    prev_start = 0
    for _ in range(num_predictions):
        pitch, step, duration = self._predict_next_note(input_notes, temperature)
        start = prev_start + step
        end = start + duration

        #adjust to the key you want
        pitch = self._adjust_pitch_to_scale(pitch, key=key)

        input_note = (pitch, step, duration)
        generated_notes.append((*input_note, start, end))

        input_notes = np.delete(input_notes, 0, axis=0)
        input_notes = np.append(input_notes, np.expand_dims(input_note, 0), axis=0)
        prev_start = start
    
        generated_notes = pd.DataFrame(generated_notes, columns=(*self.key_order, 'start', 'end'))
        
        return generated_notes








