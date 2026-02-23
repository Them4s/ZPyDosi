
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
START_DATE                (idx, [1: 24])  = 'Thu Jan 22 01:00:34 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Jan 22 20:16:58 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.21244E+00  1.00985E+00  9.93244E-01  9.87464E-01  9.93367E-01  9.97151E-01  9.93650E-01  9.98483E-01  9.82779E-01  9.86315E-01  1.00079E+00  9.92614E-01  9.98825E-01  9.95891E-01  9.96839E-01  1.00532E+00  9.87488E-01  9.91329E-01  9.97430E-01  9.97237E-01  9.84569E-01  9.88137E-01  9.96047E-01  9.85612E-01  9.95158E-01  9.75782E-01  9.87258E-01  9.89643E-01  9.83917E-01  9.95358E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 1.5E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.81105E-01 9.7E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.45798E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.45709E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.62873E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26476E+02 0.00025  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2063269185 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.43878E+05 0.00054 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00006E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.33619E+04 ;
RUNNING_TIME              (idx, 1)        =  1.15639E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.73950E-01  3.73950E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.88333E-03  9.88333E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.15601E+03  1.15601E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.15639E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85001 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88584E+01 3.3E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85728E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.22 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32926E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.14351E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.38117E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.18829E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32778E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.93667E-01 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.09776E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.73029E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82805E-01 9.5E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98777E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.28767E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.71950E-02 0.00054 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  5.99714E+01 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.42490E+00 1.4E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02241E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  9.94832E-01 5.3E-05  9.87322E-01 5.1E-05  7.49174E-03 0.00072 ];
IMP_KEFF                  (idx, [1:   2]) = [  9.94935E-01 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  9.94890E-01 4.6E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  9.94935E-01 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01237E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.10319E-03 0.00204  5.92017E-05 0.00892  3.03718E-04 0.00428  1.73383E-04 0.00543  3.92052E-04 0.00393  6.79735E-04 0.00310  2.31716E-04 0.00545  1.88260E-04 0.00562  7.51204E-05 0.00966 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.60897E-01 0.00076  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.61591E-03 0.00070  2.25217E-04 0.00404  1.09927E-03 0.00184  6.47155E-04 0.00238  1.43653E-03 0.00159  2.46237E-03 0.00123  8.13307E-04 0.00210  6.76934E-04 0.00231  2.55124E-04 0.00389 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.63274E-01 0.00110  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.76673E-05 0.00011  4.76449E-05 0.00011  5.05976E-05 0.00098 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.74202E-05 9.3E-05  4.73979E-05 9.3E-05  5.03354E-05 0.00098 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.52896E-03 0.00074  2.24417E-04 0.00436  1.08757E-03 0.00200  6.40122E-04 0.00256  1.41697E-03 0.00175  2.43309E-03 0.00133  8.05356E-04 0.00233  6.67598E-04 0.00255  2.53838E-04 0.00418 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.63746E-01 0.00120  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.69682E-05 0.00022  4.69453E-05 0.00022  4.99431E-05 0.00223 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.67247E-05 0.00021  4.67019E-05 0.00021  4.96842E-05 0.00223 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.66605E-03 0.00215  2.32259E-04 0.01242  1.10724E-03 0.00571  6.60654E-04 0.00743  1.44668E-03 0.00494  2.48177E-03 0.00381  8.02653E-04 0.00657  6.81145E-04 0.00731  2.53654E-04 0.01180 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.60688E-01 0.00336  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.67055E-03 0.00211  2.33286E-04 0.01222  1.10461E-03 0.00559  6.61276E-04 0.00725  1.44771E-03 0.00487  2.48355E-03 0.00374  8.05281E-04 0.00644  6.80901E-04 0.00715  2.53936E-04 0.01157 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.60759E-01 0.00329  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.63348E+02 0.00216 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.73329E-05 6.8E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.70875E-05 4.2E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.64289E-03 0.00041 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.61476E+02 0.00041 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.37026E-06 5.4E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96035E-06 4.8E-05  1.96019E-06 4.9E-05  1.98070E-06 0.00054 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.10601E-05 7.7E-05  7.11178E-05 7.7E-05  6.35546E-05 0.00085 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.03622E-01 2.2E-05 -3.27988E-02 0.00187  2.42121E-04 0.00188 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21859E+01 0.00111 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01232E+00 5.1E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.69297E+01 4.4E-05  1.59472E+01 6.6E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  7.00692E-01 2.9E-05  2.57740E+00 3.3E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.99690E-03 8.0E-05  2.74950E-02 3.3E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.78105E-03 6.6E-05  5.01782E-02 5.9E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.78415E-03 6.3E-05  2.26832E-02 9.7E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.68593E-03 6.6E-05  5.43973E-02 9.7E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.62642E+00 9.0E-06  2.39813E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04493E+02 7.5E-07  2.01942E+02 8.3E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.39541E-08 5.6E-05  3.57624E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.93902E-01 2.9E-05  2.52722E+00 3.5E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.53548E-01 3.3E-05  5.21011E-01 3.5E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.38075E-01 3.9E-05  8.99233E-02 9.3E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.10460E-03 0.00032  2.38256E-02 0.00029 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61961E-02 0.00016 -2.04033E-02 0.00025 ];
INF_SCATT5                (idx, [1:   4]) = [  3.41321E-05 0.07185  1.13588E-02 0.00046 ];
INF_SCATT6                (idx, [1:   4]) = [  7.31317E-03 0.00029 -3.09563E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.15971E-04 0.00218  1.06363E-02 0.00042 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.93958E-01 2.9E-05  2.52722E+00 3.5E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.53550E-01 3.3E-05  5.21011E-01 3.5E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.38077E-01 3.9E-05  8.99233E-02 9.3E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.10476E-03 0.00032  2.38256E-02 0.00029 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61960E-02 0.00016 -2.04033E-02 0.00025 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.41477E-05 0.07185  1.13588E-02 0.00046 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.31320E-03 0.00029 -3.09563E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.15954E-04 0.00218  1.06363E-02 0.00042 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.45964E-01 4.1E-05  1.72868E+00 4.0E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.35522E+00 4.1E-05  1.92826E-01 4.0E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.72464E-03 6.7E-05  5.01775E-02 5.9E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.67299E-02 4.3E-05  5.04132E-02 7.2E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 1.1E-09  1.46008E-09 0.89655 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 1.7E-07  1.95035E-07 0.89616 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.63962E-01 2.9E-05  2.99393E-02 4.1E-05  2.32202E-04 0.00070  2.52699E+00 3.5E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.44768E-01 3.3E-05  8.77942E-03 7.4E-05  1.33460E-04 0.00089  5.20878E-01 3.5E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.41139E-01 3.9E-05 -3.06349E-03 0.00017  8.42347E-05 0.00109  8.98391E-02 9.3E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.25232E-02 0.00023 -3.41856E-03 0.00013  4.32242E-05 0.00168  2.37824E-02 0.00029 ];
INF_S4                    (idx, [1:   8]) = [ -1.53948E-02 0.00016 -8.01231E-04 0.00049  1.39111E-05 0.00466 -2.04172E-02 0.00025 ];
INF_S5                    (idx, [1:   8]) = [ -3.02428E-04 0.00790  3.36560E-04 0.00106 -2.63074E-06 0.02135  1.13614E-02 0.00046 ];
INF_S6                    (idx, [1:   8]) = [  7.58023E-03 0.00028 -2.67057E-04 0.00127 -9.64166E-06 0.00544 -3.09467E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.28727E-03 0.00137 -4.71295E-04 0.00067 -1.14494E-05 0.00415  1.06477E-02 0.00041 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.64019E-01 2.9E-05  2.99393E-02 4.1E-05  2.32202E-04 0.00070  2.52699E+00 3.5E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.44771E-01 3.3E-05  8.77943E-03 7.4E-05  1.33460E-04 0.00089  5.20878E-01 3.5E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.41140E-01 3.9E-05 -3.06349E-03 0.00017  8.42347E-05 0.00109  8.98391E-02 9.3E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.25233E-02 0.00023 -3.41856E-03 0.00013  4.32242E-05 0.00168  2.37824E-02 0.00029 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53948E-02 0.00016 -8.01231E-04 0.00049  1.39111E-05 0.00466 -2.04172E-02 0.00025 ];
INF_SP5                   (idx, [1:   8]) = [ -3.02412E-04 0.00790  3.36560E-04 0.00106 -2.63076E-06 0.02135  1.13614E-02 0.00046 ];
INF_SP6                   (idx, [1:   8]) = [  7.58026E-03 0.00028 -2.67057E-04 0.00127 -9.64167E-06 0.00544 -3.09467E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.28725E-03 0.00137 -4.71295E-04 0.00067 -1.14494E-05 0.00415  1.06477E-02 0.00041 ];

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

