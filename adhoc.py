import video_files as vf
import process_video_files as pvf
#import tvf
#gpvf=vf.GPVideoFolder(tvf.folder, tvf.data)
gpvf=vf.GPVideoFolder('C:/Users/djsperka/Desktop/raw');
#pvf.concatenate_all_gpvideos(gpvf, '41636', 'PCTraining', 'c:/Users/djsperka/Desktop/out', True)
pvf.concatenate_all_gpvideos(gpvf, 'multiple', 'PairTraining', 'c:/Users/djsperka/Desktop/out', False)