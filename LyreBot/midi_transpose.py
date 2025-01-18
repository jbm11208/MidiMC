import os
import mido

NOTE_BLOCK_RANGE = range(54, 78)  # F#3 to F5

def transpose_midi(input_path, output_path):
    try:
        mid = mido.MidiFile(input_path)
    except IOError:
        print(f"Error: Cannot open {input_path}")
        return
    except mido.MidiFileError:
        print(f"Error: {input_path} is not a valid MIDI file")
        return

    transposed_mid = mido.MidiFile()
    transposed_mid.ticks_per_beat = mid.ticks_per_beat  # Preserve the tempo

    for i, track in enumerate(mid.tracks):
        transposed_track = mido.MidiTrack()
        transposed_mid.tracks.append(transposed_track)
        for msg in track:
            if msg.type == 'note_on' or msg.type == 'note_off':
                while msg.note < min(NOTE_BLOCK_RANGE):
                    msg.note += 12
                while msg.note > max(NOTE_BLOCK_RANGE):
                    msg.note -= 12
                if msg.note < 0:  # Ensure note is within valid MIDI range
                    msg.note = 0
                if msg.note > 127:  # Ensure note is within valid MIDI range
                    msg.note = 127
                transposed_track.append(msg)
            else:
                transposed_track.append(msg)
    
    transposed_mid.save(output_path)

def main():
    # Create "out" folder if it doesn't exist
    if not os.path.exists("out"):
        os.makedirs("out")

    # Transpose all MIDI files in the current directory
    for file_name in os.listdir():
        if file_name.endswith(".mid"):
            input_path = file_name
            output_path = os.path.join("out", "transposed_" + file_name)
            transpose_midi(input_path, output_path)
            print(f"Transposed MIDI file saved as {output_path}")

if __name__ == "__main__":
    main()
