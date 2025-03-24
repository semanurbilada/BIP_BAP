import os
import pandas as pd

# Define configs
num_folds = 5
fold_results = []
file_exists = os.path.exists

best_fold = None
best_mAP50 = -1  # Any valid value will be considered
best_mAP5095 = -1

for fold in range(num_folds):
    print(f"\n=== Fold {fold + 1} ===")

    # Define the result file paths
    results_file = f'../results/kfold_yolov5l_100epochs/BCCM_fold_{fold}/results.csv'
    fold_dir = f'../results/kfold_yolov5l_100epochs/BCCM_fold_{fold}/'
    # results_file = f'yolov5/runs/train/BCCM_fold_{fold}/results.csv'
    # print(os.listdir(f'yolov5/runs/train/BCCM_fold_{fold}/'))

    # Check if results file exists
    if file_exists(results_file):
        # Read CSV into a DataFrame
        results = pd.read_csv(results_file)
        print(f"Columns in Fold {fold + 1}: {results.columns.tolist()}")

        results.columns = results.columns.str.strip()  # Strip column names
        last_epoch_results = results.iloc[-1]  # Get the last row

        # Extract values from the last row
        precision = last_epoch_results.get("metrics/precision")
        recall = last_epoch_results.get("metrics/recall")
        mAP50 = last_epoch_results.get("metrics/mAP_0.5")
        mAP5095 = last_epoch_results.get("metrics/mAP_0.5:0.95")

        # If no metric is missing, add the fold results
        if None not in [precision, recall, mAP50, mAP5095]:
            fold_results.append({
                'fold': fold + 1,
                'precision': precision,
                'recall': recall,
                'mAP50': mAP50,
                'mAP50-95': mAP5095
            })
            print(f"Fold {fold + 1} - Precision: {precision}, Recall: {recall}, mAP@0.5: {mAP50}, mAP@0.5:0.95: {mAP5095}")

            # Update best fold if mAP50 is higher
            if mAP50 > best_mAP50:
                best_fold = fold + 1
                best_mAP50 = mAP50
                best_mAP5095 = mAP5095

        else:
            print(f"Some metrics are missing in Fold {fold + 1} results.")
    else:
        print(f"Results file not found for Fold {fold + 1}.")

# Calculate and display averages for the folds
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
    print("\nNo results available for averages.")

# Print overall best fold and locate best model
if best_fold is not None:
    print(f"\n=== Best Performing Fold: Fold {best_fold} ===")
    print(f"Best Fold mAP@0.5: {best_mAP50:.4f}")
    print(f"Best Fold mAP@0.95: {best_mAP5095:.4f}")

    # Locate the best model
    best_model_path = f'{fold_dir}/best.pt'
    
    if file_exists(best_model_path):
        print(f"Best model found at: {best_model_path}\n")
    else:
        print(f"Warning: best.pt file not found at {best_model_path}\n")
else:
    print("\nNo best performing fold could be determined.")