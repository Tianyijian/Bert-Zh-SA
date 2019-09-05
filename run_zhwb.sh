export BERT_BASE_DIR="/users5/yjtian/tyj/SA/BERT/chinese_L-12_H-768_A-12" # or multilingual_L-12_H-768_A-12
export ZHWB_DIR="/users5/yjtian/tyj/SA/BERT/zhwb_data"  # not use
export OUT_DIR="/users5/yjtian/tyj/SA/BERT/bert_zhwb_output"

python run_c.py \
  --task_name=ZHWB \
  --do_train=true \
  --do_eval=true \
  --data_dir=$ZHWB_DIR \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --max_seq_length=256 \
  --train_batch_size=16 \
  --learning_rate=5e-5 \
  --num_train_epochs=2.0 \
  --output_dir=$OUT_DIR