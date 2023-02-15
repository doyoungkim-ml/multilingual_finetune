#  Training experiment

CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7,8,9,11,12,13,14,15" python3 run.py --config ../configs/roe_config/xsum_1_multilingual.json
CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7,8,9,11,12,13,14,15" python3 run.py --config ../configs/roe_config/tatoeba_1_multilingual.json
CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7,8,9,11,12,13,14,15" python3 run.py --config ../configs/roe_config/tatoeba_1_multilingual_chi.json
CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7,8,9,11,12,13,14,15" python3 run.py --config ../configs/roe_config/tatoeba_1_multilingual_jap.json
CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7,8,9,11,12,13,14,15" python3 run.py --config ../configs/roe_config/tatoeba_1_multilingual_fra.json
CUDA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7,8,9,11,12,13,14,15" python3 run.py --config ../configs/roe_config/tatoeba_1_multilingual_spa.json
