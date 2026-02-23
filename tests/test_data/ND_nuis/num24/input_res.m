
% Increase counter:

if (exist('idx', 'var'));
  idx = idx + 1;
else;
  idx = 1;
end;

% Version, title and date:

VERSION                   (idx, [1: 14])  = 'Serpent 2.1.21' ;
TITLE                     (idx, [1: 13])  = 'CROCUS/PETALE' ;
INPUT_FILE_NAME           (idx, [1:  5])  = 'input' ;
START_DATE                (idx, [1: 24])  = 'Sat Jan 24 11:37:07 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Sun Jan 25 07:18:58 2026' ;

% Run parameters:

POP                       (idx, 1)        = 30000 ;
CYCLES                    (idx, 1)        = 6000 ;
SKIP                      (idx, 1)        = 50 ;
BATCH_INTERVAL            (idx, 1)        = 1 ;
SRC_NORM_MODE             (idx, 1)        = 2 ;
SEED                      (idx, 1)        = 42 ;
UFS_MODE                  (idx, 1)        = 0 ;
UFS_ORDER                 (idx, 1)        = 1.00000;
NEUTRON_TRANSPORT_MODE    (idx, 1)        = 1 ;
PHOTON_TRANSPORT_MODE     (idx, 1)        = 0 ;
GROUP_CONSTANT_GENERATION (idx, 1)        = 1 ;
B1_CALCULATION            (idx, [1:  3])  = [ 0 0 0 ];
B1_BURNUP_CORRECTION      (idx, 1)        = 0 ;
IMPLICIT_REACTION_RATES   (idx, 1)        = 1 ;
DEBUG                     (idx, 1)        = 0 ;
CPU_TYPE                  (idx, [1: 42])  = 'AMD Ryzen Threadripper PRO 5975WX 32-Cores' ;
CPU_MHZ                   (idx, 1)        = 167805455.0 ;

% Optimization:

OPTIMIZATION_MODE         (idx, 1)        = 4 ;
RECONSTRUCT_MICROXS       (idx, 1)        = 1 ;
RECONSTRUCT_MACROXS       (idx, 1)        = 1 ;
MG_MAJORANT_MODE          (idx, 1)        = 0 ;

% Parallelization:

MPI_TASKS                 (idx, 1)        = 1 ;
OMP_THREADS               (idx, 1)        = 30 ;
MPI_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_REPRODUCIBILITY       (idx, 1)        = 0 ;
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.22453E+00  9.98254E-01  9.92582E-01  1.00214E+00  9.80828E-01  1.00064E+00  9.89726E-01  9.95978E-01  1.00115E+00  9.83093E-01  9.88907E-01  9.94925E-01  9.98816E-01  1.00129E+00  9.90678E-01  9.99710E-01  9.81225E-01  9.98827E-01  9.90215E-01  9.94422E-01  9.90327E-01  9.92749E-01  9.89340E-01  9.96940E-01  9.84682E-01  9.95449E-01  9.87348E-01  9.86079E-01  9.78280E-01  9.90879E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 2.2E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.80650E-01 9.8E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.47713E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.47620E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.67247E+00 0.00021  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.25389E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2119335634 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.53223E+05 0.00050 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.40972E+04 ;
RUNNING_TIME              (idx, 1)        =  1.18185E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.75083E-01  3.75083E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.25000E-03  9.25000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.18147E+03  1.18147E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.18185E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85069 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88585E+01 3.0E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85670E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.19 ;

% Memory usage:

AVAIL_MEM                 (idx, 1)        = 257582.82 ;
ALLOC_MEMSIZE             (idx, 1)        = 29304.45;
MEMSIZE                   (idx, 1)        = 21192.67;
XS_MEMSIZE                (idx, 1)        = 4715.71;
MAT_MEMSIZE               (idx, 1)        = 1450.61;
RES_MEMSIZE               (idx, 1)        = 2.93;
MISC_MEMSIZE              (idx, 1)        = 15023.40;
UNKNOWN_MEMSIZE           (idx, 1)        = 0.00;
UNUSED_MEMSIZE            (idx, 1)        = 8111.78;

% Geometry parameters:

TOT_CELLS                 (idx, 1)        = 3455 ;
UNION_CELLS               (idx, 1)        = 19 ;

% Neutron energy grid:

NEUTRON_ERG_TOL           (idx, 1)        =  0.00000E+00 ;
NEUTRON_ERG_NE            (idx, 1)        = 1233146 ;
NEUTRON_EMIN              (idx, 1)        =  1.00000E-11 ;
NEUTRON_EMAX              (idx, 1)        =  2.00000E+01 ;

% Unresolved resonance probability table sampling:

URES_DILU_CUT             (idx, 1)        =  1.00000E-09 ;
URES_EMIN                 (idx, 1)        =  2.25000E-03 ;
URES_EMAX                 (idx, 1)        =  3.86050E-01 ;
URES_AVAIL                (idx, 1)        = 5 ;
URES_USED                 (idx, 1)        = 5 ;

% Nuclides and reaction channels:

TOT_NUCLIDES              (idx, 1)        = 64 ;
TOT_TRANSPORT_NUCLIDES    (idx, 1)        = 64 ;
TOT_DOSIMETRY_NUCLIDES    (idx, 1)        = 0 ;
TOT_DECAY_NUCLIDES        (idx, 1)        = 0 ;
TOT_PHOTON_NUCLIDES       (idx, 1)        = 0 ;
TOT_REA_CHANNELS          (idx, 1)        = 2074 ;
TOT_TRANSMU_REA           (idx, 1)        = 0 ;

% Physics options:

USE_DELNU                 (idx, 1)        = 1 ;
USE_URES                  (idx, 1)        = 1 ;
USE_DBRC                  (idx, 1)        = 0 ;
IMPL_CAPT                 (idx, 1)        = 0 ;
IMPL_NXN                  (idx, 1)        = 1 ;
IMPL_FISS                 (idx, 1)        = 0 ;
DOPPLER_PREPROCESSOR      (idx, 1)        = 0 ;
TMS_MODE                  (idx, 1)        = 0 ;
SAMPLE_FISS               (idx, 1)        = 1 ;
SAMPLE_CAPT               (idx, 1)        = 1 ;
SAMPLE_SCATT              (idx, 1)        = 1 ;

% Radioactivity data:

TOT_ACTIVITY              (idx, 1)        =  0.00000E+00 ;
TOT_DECAY_HEAT            (idx, 1)        =  0.00000E+00 ;
TOT_SF_RATE               (idx, 1)        =  0.00000E+00 ;
ACTINIDE_ACTIVITY         (idx, 1)        =  0.00000E+00 ;
ACTINIDE_DECAY_HEAT       (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_ACTIVITY  (idx, 1)        =  0.00000E+00 ;
FISSION_PRODUCT_DECAY_HEAT(idx, 1)        =  0.00000E+00 ;
INHALATION_TOXICITY       (idx, 1)        =  0.00000E+00 ;
INGESTION_TOXICITY        (idx, 1)        =  0.00000E+00 ;
SR90_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
TE132_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
I131_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
I132_ACTIVITY             (idx, 1)        =  0.00000E+00 ;
CS134_ACTIVITY            (idx, 1)        =  0.00000E+00 ;
CS137_ACTIVITY            (idx, 1)        =  0.00000E+00 ;

% Normaliation coefficient:

NORM_COEF                 (idx, [1:   4]) = [  3.32913E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.18725E-01 9.7E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.36800E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.31998E-02 0.00025 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32290E-11 3.1E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.00736E+00 3.1E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.08260E-01 3.1E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.74241E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82501E-01 9.5E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98738E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.30712E+01 3.0E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.74991E-02 0.00053 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.04933E+01 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46745E+00 1.4E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02247E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00868E+00 5.2E-05  1.00118E+00 4.9E-05  7.49405E-03 0.00072 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00865E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00864E+00 4.4E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00865E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.02664E+00 2.9E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  1.94056E-03 0.00195  5.54894E-05 0.01037  2.81034E-04 0.00422  1.59061E-04 0.00515  3.61622E-04 0.00392  6.24942E-04 0.00301  2.13440E-04 0.00524  1.74842E-04 0.00513  7.01301E-05 0.00816 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.62935E-01 0.00073  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.50408E-03 0.00068  2.22399E-04 0.00412  1.08416E-03 0.00181  6.35380E-04 0.00235  1.41571E-03 0.00157  2.42421E-03 0.00121  8.02258E-04 0.00210  6.65787E-04 0.00227  2.54183E-04 0.00367 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.64343E-01 0.00106  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.74462E-05 0.00011  4.74225E-05 0.00011  5.05737E-05 0.00097 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.78574E-05 9.3E-05  4.78335E-05 9.3E-05  5.10119E-05 0.00097 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.43205E-03 0.00074  2.20576E-04 0.00434  1.07258E-03 0.00191  6.29089E-04 0.00254  1.40034E-03 0.00172  2.40349E-03 0.00131  7.93676E-04 0.00225  6.59521E-04 0.00247  2.52772E-04 0.00405 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.64852E-01 0.00118  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.67195E-05 0.00022  4.66965E-05 0.00022  4.97465E-05 0.00220 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.71243E-05 0.00021  4.71011E-05 0.00021  5.01780E-05 0.00220 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.54213E-03 0.00210  2.29627E-04 0.01211  1.09134E-03 0.00558  6.48967E-04 0.00738  1.41900E-03 0.00488  2.43754E-03 0.00376  7.91957E-04 0.00665  6.73523E-04 0.00713  2.50172E-04 0.01163 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.61645E-01 0.00330  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.54503E-03 0.00206  2.29512E-04 0.01185  1.09241E-03 0.00547  6.49727E-04 0.00722  1.41943E-03 0.00477  2.43744E-03 0.00369  7.92294E-04 0.00647  6.73831E-04 0.00698  2.50376E-04 0.01142 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.61807E-01 0.00323  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.61568E+02 0.00212 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.70912E-05 6.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.74993E-05 4.1E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.53089E-03 0.00043 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.59926E+02 0.00044 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38101E-06 5.2E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96043E-06 4.7E-05  1.96028E-06 4.7E-05  1.98022E-06 0.00053 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.21034E-05 7.5E-05  7.21605E-05 7.6E-05  6.45581E-05 0.00084 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02198E-01 2.1E-05 -3.56407E-02 0.00173  2.58714E-04 0.00175 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21677E+01 0.00108 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.02668E+00 5.0E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.69433E+01 4.1E-05  1.61281E+01 6.9E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.99137E-01 2.9E-05  2.58286E+00 3.0E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.02428E-03 7.7E-05  2.72118E-02 3.5E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.81992E-03 6.5E-05  4.95258E-02 6.2E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.79564E-03 6.7E-05  2.23140E-02 0.00010 ];
INF_NSF                   (idx, [1:   4]) = [  4.77365E-03 6.9E-05  5.44855E-02 0.00010 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.65847E+00 9.0E-06  2.44177E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04518E+02 7.5E-07  2.01942E+02 7.8E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.38243E-08 5.8E-05  3.58150E-06 1.3E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.92309E-01 3.0E-05  2.53333E+00 3.1E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.52282E-01 3.3E-05  5.21524E-01 3.2E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37602E-01 4.1E-05  8.98616E-02 8.7E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.07298E-03 0.00034  2.38024E-02 0.00027 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61505E-02 0.00016 -2.04513E-02 0.00028 ];
INF_SCATT5                (idx, [1:   4]) = [  2.80015E-05 0.07575  1.14237E-02 0.00046 ];
INF_SCATT6                (idx, [1:   4]) = [  7.28419E-03 0.00027 -3.10367E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.10484E-04 0.00220  1.06856E-02 0.00040 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.92366E-01 3.0E-05  2.53333E+00 3.1E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.52285E-01 3.3E-05  5.21525E-01 3.2E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37604E-01 4.1E-05  8.98616E-02 8.7E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.07316E-03 0.00034  2.38024E-02 0.00027 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61504E-02 0.00016 -2.04513E-02 0.00028 ];
INF_SCATTP5               (idx, [1:   4]) = [  2.80215E-05 0.07577  1.14237E-02 0.00046 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.28420E-03 0.00027 -3.10367E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.10448E-04 0.00220  1.06856E-02 0.00040 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.45939E-01 3.9E-05  1.73420E+00 3.7E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.35535E+00 3.9E-05  1.92212E-01 3.7E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.76322E-03 6.5E-05  4.95251E-02 6.2E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.66977E-02 4.0E-05  4.97566E-02 7.6E-05 ];

% Poison cross sections:

INF_I135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_YIELD           (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_I135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_PM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MICRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_XE135_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_SM149_MACRO_ABS       (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 3.2E-09  3.97449E-09 0.79069 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  3.37259E-10 1.00000 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 4.3E-07  4.94267E-07 0.86257 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.62439E-01 2.9E-05  2.98704E-02 3.9E-05  2.29801E-04 0.00065  2.53310E+00 3.1E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.43525E-01 3.3E-05  8.75697E-03 7.5E-05  1.31764E-04 0.00088  5.21393E-01 3.2E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40658E-01 4.0E-05 -3.05531E-03 0.00016  8.31385E-05 0.00103  8.97784E-02 8.7E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24825E-02 0.00024 -3.40951E-03 0.00013  4.26614E-05 0.00161  2.37597E-02 0.00027 ];
INF_S4                    (idx, [1:   8]) = [ -1.53515E-02 0.00016 -7.99013E-04 0.00044  1.36530E-05 0.00403 -2.04649E-02 0.00028 ];
INF_S5                    (idx, [1:   8]) = [ -3.07440E-04 0.00679  3.35442E-04 0.00098 -2.57943E-06 0.02033  1.14263E-02 0.00046 ];
INF_S6                    (idx, [1:   8]) = [  7.55101E-03 0.00026 -2.66823E-04 0.00116 -9.50018E-06 0.00476 -3.10272E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.28050E-03 0.00136 -4.70016E-04 0.00066 -1.12734E-05 0.00377  1.06968E-02 0.00040 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.62496E-01 2.9E-05  2.98704E-02 3.9E-05  2.29802E-04 0.00065  2.53310E+00 3.1E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.43528E-01 3.3E-05  8.75698E-03 7.5E-05  1.31764E-04 0.00088  5.21393E-01 3.2E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40659E-01 4.0E-05 -3.05531E-03 0.00016  8.31385E-05 0.00103  8.97784E-02 8.7E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24827E-02 0.00024 -3.40951E-03 0.00013  4.26614E-05 0.00161  2.37597E-02 0.00027 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53514E-02 0.00016 -7.99014E-04 0.00044  1.36530E-05 0.00403 -2.04649E-02 0.00028 ];
INF_SP5                   (idx, [1:   8]) = [ -3.07421E-04 0.00680  3.35442E-04 0.00098 -2.57944E-06 0.02033  1.14263E-02 0.00046 ];
INF_SP6                   (idx, [1:   8]) = [  7.55103E-03 0.00026 -2.66823E-04 0.00116 -9.50018E-06 0.00476 -3.10272E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.28046E-03 0.00137 -4.70016E-04 0.00066 -1.12734E-05 0.00377  1.06968E-02 0.00040 ];

% Integral parameters:

B1_KINF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_KEFF                   (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_B2                     (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
B1_ERR                    (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];

% Critical spectrum in infinite geometry:

B1_FLX                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reaction cross sections:

B1_TOT                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CAPT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_ABS                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_FISS                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NSF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_NUBAR                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_KAPPA                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_INVV                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering cross sections:

B1_SCATT0                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT1                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT2                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT3                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT4                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT5                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT6                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATT7                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Total scattering production cross sections:

B1_SCATTP0                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP1                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP2                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP3                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP4                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP5                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP6                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SCATTP7                (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Diffusion parameters:

B1_TRANSPXS               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_DIFFCOEF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Reduced absoption and removal:

B1_RABSXS                 (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_REMXS                  (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Poison cross sections:

B1_I135_YIELD             (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_YIELD            (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_I135_MICRO_ABS         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_PM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MICRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_XE135_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SM149_MACRO_ABS        (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Fission spectra:

B1_CHIT                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHIP                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_CHID                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering matrixes:

B1_S0                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S1                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S2                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S3                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S4                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S5                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S6                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_S7                     (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

% Scattering production matrixes:

B1_SP0                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP1                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP2                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP3                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP4                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP5                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP6                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
B1_SP7                    (idx, [1:   8]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];

