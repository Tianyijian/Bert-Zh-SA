export BERT_BASE_DIR="/users5/yjtian/tyj/SA/BERT/chinese_L-12_H-768_A-12"
export ZHWB_DIR="/users5/yjtian/tyj/SA/BERT/zhwb_data"  # not use
export OUT_DIR="/users5/yjtian/tyj/SA/BERT/bert_zhwb_output"
export TRAINED_CLASSIFIER="/users5/yjtian/tyj/SA/BERT/bert_zhwb_output"

python run_c.py \
  --task_name=ZHWB \
  --do_predict=true \
  --data_dir=$ZHWB_DIR \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$TRAINED_CLASSIFIER \
  --max_seq_length=256 \
  --output_dir=$OUT_DIR