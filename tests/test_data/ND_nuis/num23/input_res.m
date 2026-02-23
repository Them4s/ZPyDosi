
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
START_DATE                (idx, [1: 24])  = 'Sat Jan 24 10:39:32 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Sun Jan 25 06:46:36 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.20534E+00  9.97588E-01  9.90636E-01  9.95648E-01  9.94658E-01  9.86718E-01  1.00274E+00  9.89579E-01  9.85369E-01  9.95184E-01  9.76491E-01  9.92191E-01  9.90224E-01  9.97627E-01  9.86922E-01  9.90010E-01  9.88918E-01  9.96668E-01  9.92660E-01  9.95619E-01  9.91749E-01  9.98755E-01  9.94913E-01  9.91133E-01  9.90521E-01  1.00241E+00  9.94552E-01  9.93889E-01  9.93697E-01  9.97582E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 1.6E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.80570E-01 9.7E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.74193E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.74093E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.73195E+00 0.00021  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.27996E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2112300778 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.52050E+05 0.00053 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.48601E+04 ;
RUNNING_TIME              (idx, 1)        =  1.20707E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.72300E-01  3.72300E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.05000E-03  9.05000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.20668E+03  1.20668E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.20706E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.88003 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88877E+01 3.0E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.86164E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.41 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32907E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.14985E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.39020E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.09802E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.33260E-11 3.1E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.01060E+00 3.1E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.11275E-01 3.1E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.70651E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.81926E-01 9.5E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98721E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.38428E+01 3.0E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.80742E-02 0.00051 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.19440E+01 5.1E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.45724E+00 1.2E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02236E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.01180E+00 5.2E-05  1.00425E+00 5.0E-05  7.55848E-03 0.00072 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.01190E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.01190E+00 4.4E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.01190E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03055E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  1.97720E-03 0.00202  5.68015E-05 0.00930  2.87027E-04 0.00431  1.62573E-04 0.00542  3.68798E-04 0.00377  6.33863E-04 0.00300  2.16426E-04 0.00515  1.81287E-04 0.00567  7.04191E-05 0.00918 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.61309E-01 0.00076  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.54085E-03 0.00068  2.24117E-04 0.00403  1.08903E-03 0.00182  6.42957E-04 0.00240  1.42461E-03 0.00159  2.43354E-03 0.00120  8.02444E-04 0.00209  6.72623E-04 0.00231  2.51537E-04 0.00384 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.62865E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.80149E-05 0.00011  4.79933E-05 0.00011  5.08647E-05 0.00098 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.85808E-05 9.4E-05  4.85588E-05 9.4E-05  5.14643E-05 0.00098 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.47099E-03 0.00074  2.21429E-04 0.00435  1.08062E-03 0.00195  6.34427E-04 0.00254  1.41073E-03 0.00172  2.41233E-03 0.00131  7.94054E-04 0.00226  6.66259E-04 0.00253  2.51141E-04 0.00417 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.63706E-01 0.00119  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.72069E-05 0.00022  4.71842E-05 0.00022  5.01445E-05 0.00221 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.77633E-05 0.00021  4.77402E-05 0.00021  5.07360E-05 0.00221 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.58938E-03 0.00216  2.32492E-04 0.01217  1.09949E-03 0.00565  6.48692E-04 0.00738  1.42671E-03 0.00504  2.46538E-03 0.00375  8.04802E-04 0.00657  6.62050E-04 0.00735  2.49772E-04 0.01188 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.58426E-01 0.00338  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.58821E-03 0.00212  2.30785E-04 0.01198  1.09889E-03 0.00555  6.47213E-04 0.00719  1.42820E-03 0.00496  2.46566E-03 0.00370  8.05619E-04 0.00643  6.62031E-04 0.00721  2.49810E-04 0.01163 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.58655E-01 0.00330  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.60899E+02 0.00218 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.76136E-05 6.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.81747E-05 4.2E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.58144E-03 0.00041 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.59233E+02 0.00042 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.39993E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96101E-06 4.7E-05  1.96086E-06 4.7E-05  1.98155E-06 0.00055 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.43905E-05 7.7E-05  7.44542E-05 7.7E-05  6.59759E-05 0.00086 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.03032E-01 2.1E-05 -3.47962E-02 0.00183  2.52842E-04 0.00185 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21715E+01 0.00110 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.03060E+00 5.3E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.72397E+01 4.5E-05  1.66033E+01 6.8E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.92200E-01 2.8E-05  2.59521E+00 2.8E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.94971E-03 8.0E-05  2.62494E-02 3.4E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.70137E-03 6.4E-05  4.81464E-02 6.0E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.75167E-03 5.6E-05  2.18970E-02 9.8E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.61286E-03 5.8E-05  5.33000E-02 9.8E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.63341E+00 7.9E-06  2.43412E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04481E+02 7.7E-07  2.01942E+02 7.5E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.31962E-08 5.3E-05  3.59304E-06 1.3E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.85491E-01 2.8E-05  2.54706E+00 2.9E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.49573E-01 3.0E-05  5.23460E-01 3.2E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.36683E-01 3.5E-05  8.98880E-02 8.9E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.13861E-03 0.00028  2.37886E-02 0.00027 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.59149E-02 0.00016 -2.06433E-02 0.00027 ];
INF_SCATT5                (idx, [1:   4]) = [  7.80404E-05 0.02793  1.15111E-02 0.00045 ];
INF_SCATT6                (idx, [1:   4]) = [  7.25002E-03 0.00028 -3.12796E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.15441E-04 0.00226  1.08232E-02 0.00041 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.85547E-01 2.8E-05  2.54706E+00 2.9E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.49576E-01 3.0E-05  5.23460E-01 3.2E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.36684E-01 3.5E-05  8.98880E-02 8.9E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.13882E-03 0.00028  2.37886E-02 0.00027 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.59149E-02 0.00016 -2.06433E-02 0.00027 ];
INF_SCATTP5               (idx, [1:   4]) = [  7.80502E-05 0.02793  1.15111E-02 0.00045 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.25004E-03 0.00028 -3.12796E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.15451E-04 0.00226  1.08233E-02 0.00041 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.40226E-01 3.8E-05  1.74385E+00 3.4E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.38759E+00 3.8E-05  1.91149E-01 3.4E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.64515E-03 6.5E-05  4.81457E-02 6.0E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.62838E-02 4.4E-05  4.83697E-02 7.6E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 9.3E-10  2.16228E-09 0.56636 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 1.7E-07  2.92516E-07 0.56605 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.55916E-01 2.7E-05  2.95750E-02 3.8E-05  2.22438E-04 0.00067  2.54684E+00 2.9E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.40900E-01 3.0E-05  8.67298E-03 7.8E-05  1.27943E-04 0.00083  5.23332E-01 3.2E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.39708E-01 3.4E-05 -3.02524E-03 0.00018  8.07437E-05 0.00099  8.98073E-02 8.9E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.25149E-02 0.00021 -3.37626E-03 0.00013  4.14081E-05 0.00157  2.37472E-02 0.00027 ];
INF_S4                    (idx, [1:   8]) = [ -1.51231E-02 0.00016 -7.91752E-04 0.00051  1.32027E-05 0.00424 -2.06565E-02 0.00027 ];
INF_S5                    (idx, [1:   8]) = [ -2.54234E-04 0.00851  3.32274E-04 0.00103 -2.51718E-06 0.02142  1.15136E-02 0.00045 ];
INF_S6                    (idx, [1:   8]) = [  7.51335E-03 0.00026 -2.63325E-04 0.00122 -9.19275E-06 0.00573 -3.12704E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.28100E-03 0.00142 -4.65558E-04 0.00068 -1.09582E-05 0.00416  1.08342E-02 0.00041 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.55972E-01 2.7E-05  2.95750E-02 3.8E-05  2.22439E-04 0.00067  2.54684E+00 2.9E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.40903E-01 3.0E-05  8.67298E-03 7.8E-05  1.27943E-04 0.00083  5.23332E-01 3.2E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.39709E-01 3.4E-05 -3.02524E-03 0.00018  8.07437E-05 0.00099  8.98073E-02 8.9E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.25151E-02 0.00021 -3.37626E-03 0.00013  4.14081E-05 0.00157  2.37472E-02 0.00027 ];
INF_SP4                   (idx, [1:   8]) = [ -1.51231E-02 0.00016 -7.91752E-04 0.00051  1.32027E-05 0.00424 -2.06565E-02 0.00027 ];
INF_SP5                   (idx, [1:   8]) = [ -2.54224E-04 0.00851  3.32274E-04 0.00103 -2.51718E-06 0.02142  1.15136E-02 0.00045 ];
INF_SP6                   (idx, [1:   8]) = [  7.51337E-03 0.00026 -2.63325E-04 0.00122 -9.19276E-06 0.00573 -3.12704E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.28101E-03 0.00142 -4.65558E-04 0.00068 -1.09582E-05 0.00416  1.08342E-02 0.00041 ];

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

