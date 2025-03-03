import os
import pandas as pd

# Define configs
num_folds = 5
fold_results = []
file_exists = os.path.exists

for fold in range(num_folds):
    print(f"\n=== Fold {fold + 1} ===")

    # results_file = f'yolov5/runs/train/BCCM_fold_{fold}/results.csv'
    # print(os.listdir(f'yolov5/runs/train/BCCM_fold_{fold}/'))
    results_file = f'../results/kfold_9_yolov5l_100epochs/BCCM_fold_{fold}/results.csv'
    print(os.listdir(f'../results/kfold_9_yolov5l_100epochs/BCCM_fold_{fold}/'))

    if file_exists(results_file):
        results = pd.read_csv(results_file)
        print(f"Columns in Fold {fold + 1}: {results.columns.tolist()}")
        
        results.columns = results.columns.str.strip()
        last_epoch_results = results.iloc[-1]

        # Column names from results.csv
        precision = last_epoch_results.get("metrics/precision", None)
        recall = last_epoch_results.get("metrics/recall", None)

        mAP50 = last_epoch_results.get("metrics/mAP_0.5", None)
        mAP5095 = last_epoch_results.get("metrics/mAP_0.5:0.95", None)

        if None not in [precision, recall, mAP50, mAP5095]:
            fold_results.append({
                'fold': fold + 1,
                'precision': precision,
                'recall': recall,
                'mAP50': mAP50,
                'mAP50-95': mAP5095
            })
            print(f"Fold {fold + 1} - Precision: {precision}, Recall: {recall}, mAP@0.5: {mAP50}, mAP@0.5:0.95: {mAP5095}")
        else:
            print(f"Some metrics are missing in Fold {fold + 1} results.")
    else:
        print(f"Results file not found for Fold {fold + 1}.")

# Calculate and display averages
if fold_results:
    results_df = pd.DataFrame(fold_results)
    avg_precision = results_df['precision'].mean()
    avg_recall = results_df['recall'].mean()
    avg_map50 = results_df['mAP50'].mean()
    avg_map5095 = results_df['mAP50-95'].mean()
    
    print("\n=== Final Cross-Validation Results ===")
    print(f"Overall Average Precision: {avg_precision:.4f}")
    print(f"Overall Average Recall: {avg_recall:.4f}")
    print(f"Overall Average mAP@0.5: {avg_map50:.4f}")
    print(f"Overall Average mAP@0.5:0.95: {avg_map5095:.4f}")
else:
    print("No results available for averages.")