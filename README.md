# Computational Recapitulation of Immune Selection: An Integrated Deep Learning Pipeline for De Novo Human Antibody Discovery


## design_activin/zdock_redo_new: contains the large scale bind site restricted zdock script 

bash  run_batch1.bash  (runing docking)

## design_new_antibody_activin/complex_train_redo_structure_based_reduce_usage_activin :   complex structure based antibody-antigen binding prediction

bash run_all_pos.bash  (preparation input graph data)

bash run_all_pred.bash  (running)

## design_new_antibody_activin/complex_train_redo_usage_activin:   non-complex structure based antibody-antigen binding prediction

bash run_all_pos.bash  (preparation input graph data)

bash run_all_pred.bash  (running)

## design_new_antibody_activin/static_eval:     static based antibody-antigen screening(cutoff 0.6nm)

bash run_score.bash

## design_new_antibody_activin/static_eval_cutoff10 :    static based antibody-antigen screening(cutoff 1nm)

bash run_score.bash

## complex_train_redo_CDR_fast_n: contains the DeepCDR_Bind training code

bash run_all_pos.bash  (preparation input graph data)

python  training_nn3_PP.py  (training)

## complex_train_redo_CDR_fast_n_usage:  contains the DeepCDR_Bind usage script

bash run_all_pos.bash  (preparation input graph data)

bash run_all_predict.bash (running)

