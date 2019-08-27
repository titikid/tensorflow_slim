#!/usr/bin/env bash
#
# height = (clip_duration_ms - window_size_ms + window_stride_ms) / window_stride_ms
# clip_duration_ms = (height*window_stride_ms) + window_size_ms - window_stride_ms
# width  = dct_coefficient_count
#
# input: 98x40
# if win_size=30ms and win_stride=10ms, clip_duration_ms = 98*10+30-10 = 1000ms
#
# input: 2*32x32
# if win_size=32ms and win_stride=16ms, clip_duration_ms = 2*32*16+32-16 = 1040ms

NETWORK=binary3a_conv
NET_ID=cmd_seven
TRAIN_DIR=/home/atsg/PycharmProjects/gvh205_py2/Lattice_BNN/KeyPhrase_Package/seven/training/checkpoint

TRAIN_OPT=--optimizer=Adam
#TRAIN_OPT="$TRAIN_OPT --start_checkpoint=$TRAIN_DIR/$NETWORK.ckpt-50000"
#TRAIN_OPT="$TRAIN_OPT --set_prefilter=/tmp/set6_robot/tinyex2_conv.ckpt-70000"

COMMON_OPT="--wanted_words=seven \
--model_architecture=$NETWORK \
--sample_rate=16000 \
--downsample=4 \
--no_prefilter_bias \
--clip_duration_ms=1040 \
--time_shift_ms=140.0 \
--window_size_ms=32.0 \
--window_stride_ms=16.0 \
--dct_coefficient_count=32 \
--background_volume=0.5"

if [[ $TRAIN_OPT != *"start_checkpoint"* ]]; then
  rm -rf /tmp/$NET_ID
fi

python3 freeze.py \
$COMMON_OPT \
--start_checkpoint=$TRAIN_DIR/$NETWORK.ckpt-2000 \
--output_file=$TRAIN_DIR/$NETWORK-2000.pb \
--norm_binw
