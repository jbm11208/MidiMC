﻿using Melanchall.DryWetMidi.Core;
using System.Linq;

namespace LyreBot.Models
{
    public class MidiTrackModel
    {
        private bool _isChecked = true;

        public string TrackName { get; private set; }
        public TrackChunk Track { get; private set; }
        public bool IsChecked
        {
            get => true;
            set
            {
                _isChecked = value;
                ViewModels.MainViewModel.reloadPlayback = true;
            }
        }

        public MidiTrackModel(TrackChunk track)
        {
            Track = track;
            TrackName = track.Events.OfType<SequenceTrackNameEvent>().FirstOrDefault()?.Text;
        }

        public MidiTrackModel(TrackChunk track, bool isChecked)
        {
            Track = track;
            TrackName = track.Events.OfType<SequenceTrackNameEvent>().FirstOrDefault()?.Text;
            IsChecked = isChecked;
        }
    }
}
