
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
START_DATE                (idx, [1: 24])  = 'Fri Jan 23 15:51:38 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Sat Jan 24 11:37:03 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.21454E+00  1.01030E+00  9.89670E-01  9.89053E-01  9.94677E-01  1.00045E+00  9.91547E-01  9.95541E-01  9.96894E-01  9.96517E-01  9.84770E-01  9.93030E-01  1.00139E+00  9.88711E-01  9.96704E-01  9.89058E-01  9.93523E-01  9.79743E-01  9.99700E-01  9.89840E-01  9.87893E-01  9.76950E-01  9.88225E-01  9.98902E-01  9.92282E-01  9.84281E-01  9.87140E-01  9.91403E-01  1.00247E+00  9.94804E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 1.7E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.80657E-01 9.1E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.59397E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.59299E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.69493E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.27406E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2096117628 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.49353E+05 0.00052 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.42133E+04 ;
RUNNING_TIME              (idx, 1)        =  1.18542E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.72450E-01  3.72450E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.40000E-03  9.40000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.18504E+03  1.18504E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.18542E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.86165 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88694E+01 3.0E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85890E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.29 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32884E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.17209E-01 9.9E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.39103E-01 1.6E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.08971E-02 0.00025 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32047E-11 3.1E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.92410E-01 3.1E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.07529E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.74723E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82252E-01 9.3E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98653E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.35009E+01 3.0E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.77478E-02 0.00051 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.09989E+01 4.9E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.43519E+00 1.4E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02236E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  9.93692E-01 5.2E-05  9.86210E-01 4.9E-05  7.46954E-03 0.00072 ];
IMP_KEFF                  (idx, [1:   2]) = [  9.93690E-01 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  9.93755E-01 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  9.93690E-01 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01167E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.01805E-03 0.00185  5.69990E-05 0.00814  2.91217E-04 0.00409  1.67103E-04 0.00537  3.76311E-04 0.00355  6.51996E-04 0.00294  2.21480E-04 0.00482  1.82323E-04 0.00534  7.06174E-05 0.00869 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.60191E-01 0.00074  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.60009E-03 0.00068  2.24822E-04 0.00400  1.10206E-03 0.00181  6.45696E-04 0.00238  1.43363E-03 0.00156  2.45694E-03 0.00122  8.09098E-04 0.00213  6.76274E-04 0.00231  2.51580E-04 0.00373 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.61848E-01 0.00106  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.82803E-05 0.00011  4.82586E-05 0.00011  5.11278E-05 0.00096 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.79750E-05 9.3E-05  4.79534E-05 9.3E-05  5.08045E-05 0.00096 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.52092E-03 0.00074  2.22296E-04 0.00433  1.09023E-03 0.00195  6.38669E-04 0.00260  1.41614E-03 0.00170  2.43346E-03 0.00131  8.01395E-04 0.00227  6.68190E-04 0.00253  2.50535E-04 0.00412 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.62416E-01 0.00117  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.75166E-05 0.00022  4.74942E-05 0.00022  5.04513E-05 0.00221 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.72161E-05 0.00021  4.71938E-05 0.00021  5.01323E-05 0.00221 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.62950E-03 0.00211  2.29396E-04 0.01243  1.11281E-03 0.00563  6.40110E-04 0.00732  1.43174E-03 0.00488  2.46663E-03 0.00372  8.07749E-04 0.00653  6.85162E-04 0.00718  2.55896E-04 0.01205 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.63763E-01 0.00335  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.62457E-03 0.00207  2.28933E-04 0.01220  1.11168E-03 0.00551  6.40570E-04 0.00717  1.43072E-03 0.00479  2.46264E-03 0.00364  8.08287E-04 0.00645  6.85358E-04 0.00704  2.56381E-04 0.01187 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.64231E-01 0.00330  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.60683E+02 0.00212 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.79123E-05 6.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.76093E-05 4.2E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.62060E-03 0.00041 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.59057E+02 0.00041 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38234E-06 5.2E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96185E-06 4.8E-05  1.96169E-06 4.8E-05  1.98232E-06 0.00053 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.28483E-05 7.5E-05  7.29089E-05 7.6E-05  6.49253E-05 0.00086 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02963E-01 2.1E-05 -3.42818E-02 0.00174  2.51482E-04 0.00175 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.22160E+01 0.00110 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01176E+00 5.0E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.72085E+01 4.3E-05  1.62925E+01 6.3E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.93689E-01 2.8E-05  2.58555E+00 3.1E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.95385E-03 8.5E-05  2.70026E-02 3.3E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.71921E-03 7.0E-05  4.90680E-02 5.6E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.76536E-03 6.1E-05  2.20654E-02 9.1E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.65582E-03 6.3E-05  5.31373E-02 9.1E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.63732E+00 8.5E-06  2.40818E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04439E+02 7.5E-07  2.01942E+02 7.3E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.33433E-08 5.3E-05  3.58510E-06 1.3E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.86963E-01 2.8E-05  2.53648E+00 3.2E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.49895E-01 3.1E-05  5.22481E-01 3.4E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.36700E-01 3.7E-05  8.99275E-02 8.8E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.07770E-03 0.00029  2.38128E-02 0.00027 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.59725E-02 0.00016 -2.05441E-02 0.00027 ];
INF_SCATT5                (idx, [1:   4]) = [  5.83720E-05 0.03931  1.14497E-02 0.00046 ];
INF_SCATT6                (idx, [1:   4]) = [  7.24114E-03 0.00027 -3.11420E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.10749E-04 0.00211  1.07403E-02 0.00041 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.87020E-01 2.8E-05  2.53648E+00 3.2E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.49898E-01 3.1E-05  5.22481E-01 3.4E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.36702E-01 3.7E-05  8.99275E-02 8.8E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.07790E-03 0.00029  2.38128E-02 0.00027 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.59724E-02 0.00016 -2.05441E-02 0.00027 ];
INF_SCATTP5               (idx, [1:   4]) = [  5.83816E-05 0.03930  1.14497E-02 0.00046 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.24119E-03 0.00027 -3.11421E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.10714E-04 0.00211  1.07403E-02 0.00041 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.42752E-01 4.0E-05  1.73443E+00 3.7E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.37314E+00 4.0E-05  1.92186E-01 3.7E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.66270E-03 7.0E-05  4.90673E-02 5.6E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.63295E-02 4.2E-05  4.92935E-02 7.0E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 9.3E-10  2.72181E-10 0.72076 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 2.6E-08  3.61635E-08 0.72434 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.57360E-01 2.7E-05  2.96038E-02 4.0E-05  2.25884E-04 0.00067  2.53625E+00 3.2E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.41208E-01 3.1E-05  8.68693E-03 7.9E-05  1.30098E-04 0.00086  5.22351E-01 3.4E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.39730E-01 3.6E-05 -3.02969E-03 0.00017  8.22194E-05 0.00101  8.98453E-02 8.8E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24582E-02 0.00021 -3.38046E-03 0.00013  4.22059E-05 0.00166  2.37706E-02 0.00027 ];
INF_S4                    (idx, [1:   8]) = [ -1.51804E-02 0.00016 -7.92051E-04 0.00050  1.34688E-05 0.00425 -2.05576E-02 0.00027 ];
INF_S5                    (idx, [1:   8]) = [ -2.74520E-04 0.00830  3.32892E-04 0.00102 -2.66412E-06 0.01912  1.14523E-02 0.00046 ];
INF_S6                    (idx, [1:   8]) = [  7.50571E-03 0.00026 -2.64567E-04 0.00126 -9.46247E-06 0.00511 -3.11326E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.27718E-03 0.00130 -4.66432E-04 0.00063 -1.12403E-05 0.00403  1.07515E-02 0.00041 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.57416E-01 2.7E-05  2.96038E-02 4.0E-05  2.25885E-04 0.00067  2.53625E+00 3.2E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.41211E-01 3.1E-05  8.68693E-03 7.9E-05  1.30098E-04 0.00086  5.22351E-01 3.4E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.39731E-01 3.6E-05 -3.02969E-03 0.00017  8.22194E-05 0.00101  8.98453E-02 8.8E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24584E-02 0.00021 -3.38046E-03 0.00013  4.22059E-05 0.00166  2.37706E-02 0.00027 ];
INF_SP4                   (idx, [1:   8]) = [ -1.51804E-02 0.00016 -7.92051E-04 0.00050  1.34688E-05 0.00425 -2.05576E-02 0.00027 ];
INF_SP5                   (idx, [1:   8]) = [ -2.74511E-04 0.00830  3.32892E-04 0.00102 -2.66413E-06 0.01912  1.14523E-02 0.00046 ];
INF_SP6                   (idx, [1:   8]) = [  7.50576E-03 0.00026 -2.64567E-04 0.00126 -9.46247E-06 0.00511 -3.11326E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.27715E-03 0.00130 -4.66432E-04 0.00063 -1.12403E-05 0.00403  1.07515E-02 0.00041 ];

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

