ALL_DATA_TYPES = ['training', 'test', 'validation']
ALL_METRICES = ['ccc', 'corr', 'mae', 'mse', 'wf1', 'acc']
ALL_LOSS = ['ccc', 'corr', 'ce', 'mae', 'mse', 'wf1', 'acc', 'mae+corr', 'mae+corr+ce', 'mae+ccc', 'mae+corr+ccc']

MODALITY_FEATURE_SIZE = {
    'vision': 125, 'acoustic': 140, 'language': 457,
    'eda': 62, 'ecg': 54, #'mocap': 330, 
}

MODALITY_HIDDEN_DIM = {
    'vision': 188, 'acoustic': 210, 'language': 686,
    'eda': 96, 'ecg': 82
}

ALL_MODALITIES = [
    'vision', 'acoustic', 'language', 
    'eda', 'ecg', 
]

ALL_MODALITY_PAIRS = [
    ['vision', 'language'],
    ['vision', 'acoustic'],
    ['vision', 'mocap'],
    ['vision', 'ecg'],
    ['vision', 'eda'],
    ['language', 'acoustic'],
    ['language', 'mocap'],
    ['language', 'ecg'],
    ['language', 'eda'],
    ['acoustic', 'mocap'],
    ['acoustic', 'ecg'],
    ['acoustic', 'eda'],
    ['mocap', 'ecg'],
    ['mocap', 'eda'],
    ['ecg', 'eda']
]

ALL_MODALITY_TRIPLETS = [
    ['vision', 'acoustic', 'language'],
    ['vision', 'ecg', 'eda'],
    ['vision', 'mocap', 'acoustic'],
    ['vision', 'mocap', 'language'],
    ['mocap', 'acoustic', 'language'],
    ['vision', 'acoustic', 'ecg'],
    ['vision', 'acoustic', 'eda'],
    ['vision', 'ecg', 'eda'],
    ['acoustic', 'ecg', 'eda'],
]

ALL_MODALITY_QUADRUAPLETS = [
    ['vision', 'mocap', 'acoustic', 'language']
]

SUB_MODALITY_SET = [
    ['vision'], ['language'], ['acoustic'], ['mocap'], ['ecg'], ['eda'],
] + ALL_MODALITY_PAIRS + ALL_MODALITY_TRIPLETS + ALL_MODALITY_QUADRUAPLETS

ALL_DATASETS = ['iemocap_valence', 'iemocap_arousal',
                'recola_valence', 'recola_arousal', 
                'sewa_valence', 'sewa_arousal', 'mosi_sentiment',
                'mosei_sentiment', 'mosei_happiness',
                ]

MODALITY_DATASET = {
    'vision': [
        'umeme_valence', 'vreed_av',
        'tpot_constructs', 'iemocap_valence',
        'recola_valence',  'mosi_sentiment',
        'sewa_valence', 'umeme_arousal',
        'mosei_happiness', 'recola_arousal',
        'sewa_arousal', 'iemocap_arousal',
        'mosei_sentiment',
    ],
    'language': [
        'umeme_valence', 'tpot_constructs', 
        'iemocap_valence', 'mosi_sentiment',
        'sewa_valence', 'umeme_arousal',
        'mosei_happiness', 'sewa_arousal', 
        'iemocap_arousal', 'mosei_sentiment',
    ],
    'acoustic': [
        'umeme_valence', 'tpot_constructs', 
        'iemocap_valence', 'recola_valence', 
        'mosi_sentiment', 'sewa_valence', 
        'umeme_arousal', 'mosei_happiness', 
        'recola_arousal', 'sewa_arousal', 
        'iemocap_arousal', 'mosei_sentiment',
    ],
    'mocap': [
        'iemocap_valence', 'iemocap_arousal'
    ],
    'ecg': [
        'vreed_av', 'recola_valence', 'recola_arousal'
    ],
    'eda': [
        'vreed_av', 'recola_valence', 'recola_arousal'
    ]
}

DATASET_MODALITY = {
    'iemocap_valence': ['vision', 'acoustic', 'language'],
    'recola_valence': ['vision', 'acoustic', 'ecg', 'eda'],
    'mosi_sentiment': ['vision', 'acoustic', 'language'],
    'sewa_valence': ['vision', 'acoustic', 'language'],
    'umeme_arousal': ['vision', 'acoustic', 'language'],
    'mosei_happiness': ['vision', 'acoustic', 'language'],
    'recola_arousal': ['vision', 'acoustic', 'ecg', 'eda'],
    'sewa_arousal': ['vision', 'acoustic', 'language'],
    'iemocap_arousal': ['vision', 'acoustic', 'language'],
    'mosei_sentiment': ['vision', 'acoustic', 'language'],
}

"""
R means regression and C means classification
"""
DATASET_TASK = {
    'umeme_valence': 'R',
    'vreed_av': 'C',
    'tpot_constructs': 'C',
    'iemocap_valence': 'R',
    'recola_valence': 'R',
    'mosi_sentiment': 'R',
    'sewa_valence': 'R',
    'umeme_arousal': 'R',
    'mosei_happiness': 'R',
    'recola_arousal': 'R',
    'sewa_arousal': 'R',
    'iemocap_arousal': 'R',
    'mosei_sentiment': 'R',
}

DATASET_CLASS_NUMBER = {
    'umeme_valence': None,
    'vreed_av': 4,
    'tpot_constructs': 4,
    'iemocap_valence': None,
    'recola_valence': None,
    'mosi_sentiment': None,
    'sewa_valence': None,
    'umeme_arousal': None,
    'mosei_happiness': None,
    'recola_arousal': None,
    'sewa_arousal': None,
    'iemocap_arousal': None,
    'mosei_sentiment': None,
}
