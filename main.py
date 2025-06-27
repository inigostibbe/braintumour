import fiftyone as fo
import fiftyone.zoo as foz

dir = r'G:\My Drive\Coding Stuff\PROJECTS\braintumour\archive\brain_tumor_dataset'

dataset = fo.Dataset.from_dir(
    dataset_type=fo.types.ImageClassificationDirectoryTree,
    dataset_dir=dir
)

session = fo.launch_app(dataset)
