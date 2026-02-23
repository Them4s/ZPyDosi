
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
START_DATE                (idx, [1: 24])  = 'Sun Jan 25 06:46:39 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Mon Jan 26 02:23:46 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.19334E+00  1.01325E+00  9.92349E-01  9.96607E-01  9.97072E-01  9.93397E-01  9.96170E-01  1.00095E+00  9.95470E-01  9.95176E-01  9.91901E-01  9.91624E-01  9.89223E-01  9.88881E-01  9.94841E-01  9.96934E-01  9.89052E-01  9.95309E-01  9.87746E-01  9.54935E-01  1.00027E+00  1.00101E+00  9.96482E-01  9.99184E-01  9.92741E-01  9.93616E-01  9.92358E-01  9.94655E-01  9.94846E-01  9.80616E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 0.0E+00  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.80207E-01 9.5E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.47297E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.47203E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.71079E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.25585E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2102882453 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.50480E+05 0.00051 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00007 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.39651E+04 ;
RUNNING_TIME              (idx, 1)        =  1.17712E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.71017E-01  3.71017E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.50000E-03  9.50000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.17673E+03  1.17673E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.17711E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85455 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88624E+01 3.1E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85663E-01 ;
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

NORM_COEF                 (idx, [1:   4]) = [  3.32925E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.17066E-01 9.7E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.34257E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.57429E-02 0.00024 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.33194E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.00495E+00 3.1E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.11023E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.71240E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82263E-01 9.3E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98775E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.30166E+01 3.0E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.77367E-02 0.00051 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.03517E+01 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44498E+00 1.5E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02259E+02 1.5E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00619E+00 5.1E-05  9.98638E-01 4.8E-05  7.55545E-03 0.00071 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00622E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00618E+00 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00622E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.02441E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  1.99446E-03 0.00194  5.57291E-05 0.00823  2.88388E-04 0.00425  1.63867E-04 0.00502  3.71367E-04 0.00352  6.41862E-04 0.00285  2.21576E-04 0.00495  1.79869E-04 0.00536  7.17993E-05 0.00819 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.64023E-01 0.00075  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.58699E-03 0.00068  2.23486E-04 0.00404  1.09305E-03 0.00178  6.41588E-04 0.00234  1.42815E-03 0.00158  2.44573E-03 0.00117  8.19578E-04 0.00211  6.76021E-04 0.00231  2.59383E-04 0.00385 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.66505E-01 0.00109  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.76167E-05 0.00010  4.75929E-05 0.00010  5.07381E-05 0.00096 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.79108E-05 9.2E-05  4.78868E-05 9.2E-05  5.10516E-05 0.00096 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.50738E-03 0.00073  2.21694E-04 0.00437  1.08074E-03 0.00195  6.36777E-04 0.00254  1.41125E-03 0.00171  2.42095E-03 0.00128  8.10175E-04 0.00228  6.69640E-04 0.00246  2.56158E-04 0.00404 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.66426E-01 0.00116  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.69118E-05 0.00022  4.68878E-05 0.00022  5.00316E-05 0.00219 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.72015E-05 0.00021  4.71774E-05 0.00021  5.03394E-05 0.00219 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.64913E-03 0.00214  2.32160E-04 0.01261  1.09708E-03 0.00561  6.57794E-04 0.00729  1.44826E-03 0.00487  2.46084E-03 0.00374  8.16269E-04 0.00647  6.83053E-04 0.00717  2.53670E-04 0.01179 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.62402E-01 0.00328  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.65164E-03 0.00210  2.30527E-04 0.01228  1.09695E-03 0.00551  6.59474E-04 0.00721  1.44977E-03 0.00482  2.46362E-03 0.00367  8.15957E-04 0.00638  6.81973E-04 0.00707  2.53375E-04 0.01153 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.62008E-01 0.00322  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.63184E+02 0.00215 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.72819E-05 6.4E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.75739E-05 4.0E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.61522E-03 0.00042 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.61065E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38512E-06 5.2E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96084E-06 4.7E-05  1.96068E-06 4.7E-05  1.98272E-06 0.00053 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.23268E-05 7.5E-05  7.23850E-05 7.5E-05  6.47620E-05 0.00083 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.01138E-01 2.1E-05 -3.43443E-02 0.00172  2.53435E-04 0.00176 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21490E+01 0.00109 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.02440E+00 4.9E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.68620E+01 4.2E-05  1.61548E+01 6.2E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.96951E-01 2.8E-05  2.57698E+00 2.8E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.04034E-03 7.5E-05  2.69797E-02 3.2E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.87449E-03 6.2E-05  4.93729E-02 5.7E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.83415E-03 6.2E-05  2.23932E-02 9.2E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.86871E-03 6.4E-05  5.41122E-02 9.2E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.65447E+00 8.3E-06  2.41645E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04591E+02 7.4E-07  2.01942E+02 7.9E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.39106E-08 5.0E-05  3.58204E-06 1.3E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.90068E-01 2.8E-05  2.52761E+00 2.9E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.52697E-01 3.2E-05  5.21128E-01 3.3E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37767E-01 3.6E-05  8.98003E-02 9.6E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.06806E-03 0.00030  2.37824E-02 0.00029 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61848E-02 0.00016 -2.04603E-02 0.00030 ];
INF_SCATT5                (idx, [1:   4]) = [  2.97706E-05 0.07385  1.14170E-02 0.00045 ];
INF_SCATT6                (idx, [1:   4]) = [  7.30407E-03 0.00030 -3.10175E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.15004E-04 0.00231  1.06818E-02 0.00040 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.90124E-01 2.8E-05  2.52761E+00 2.9E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.52700E-01 3.2E-05  5.21128E-01 3.3E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37769E-01 3.6E-05  8.98003E-02 9.6E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.06826E-03 0.00030  2.37824E-02 0.00029 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61847E-02 0.00016 -2.04603E-02 0.00030 ];
INF_SCATTP5               (idx, [1:   4]) = [  2.97544E-05 0.07385  1.14170E-02 0.00045 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.30409E-03 0.00030 -3.10175E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.15004E-04 0.00231  1.06818E-02 0.00040 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.44507E-01 3.7E-05  1.72804E+00 3.5E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.36329E+00 3.7E-05  1.92896E-01 3.5E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.81827E-03 6.2E-05  4.93722E-02 5.7E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.68043E-02 4.0E-05  4.96011E-02 7.1E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  7.29435E-10 0.87815 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 8.2E-08  9.38520E-08 0.87375 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.60147E-01 2.8E-05  2.99209E-02 3.8E-05  2.26618E-04 0.00066  2.52738E+00 2.9E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.43914E-01 3.2E-05  8.78344E-03 7.8E-05  1.31071E-04 0.00087  5.20997E-01 3.3E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40828E-01 3.6E-05 -3.06096E-03 0.00017  8.29154E-05 0.00112  8.97174E-02 9.7E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24856E-02 0.00021 -3.41750E-03 0.00013  4.25430E-05 0.00173  2.37399E-02 0.00029 ];
INF_S4                    (idx, [1:   8]) = [ -1.53832E-02 0.00016 -8.01582E-04 0.00048  1.36040E-05 0.00409 -2.04739E-02 0.00030 ];
INF_S5                    (idx, [1:   8]) = [ -3.06318E-04 0.00698  3.36088E-04 0.00103 -2.60996E-06 0.01893  1.14197E-02 0.00045 ];
INF_S6                    (idx, [1:   8]) = [  7.57071E-03 0.00029 -2.66640E-04 0.00120 -9.47633E-06 0.00523 -3.10080E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.28603E-03 0.00146 -4.71024E-04 0.00063 -1.13506E-05 0.00404  1.06931E-02 0.00040 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.60203E-01 2.8E-05  2.99209E-02 3.8E-05  2.26618E-04 0.00066  2.52738E+00 2.9E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.43916E-01 3.2E-05  8.78344E-03 7.8E-05  1.31071E-04 0.00087  5.20997E-01 3.3E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40830E-01 3.6E-05 -3.06096E-03 0.00017  8.29154E-05 0.00112  8.97174E-02 9.7E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24858E-02 0.00021 -3.41750E-03 0.00013  4.25430E-05 0.00173  2.37399E-02 0.00029 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53832E-02 0.00016 -8.01582E-04 0.00048  1.36040E-05 0.00409 -2.04739E-02 0.00030 ];
INF_SP5                   (idx, [1:   8]) = [ -3.06334E-04 0.00697  3.36089E-04 0.00103 -2.60996E-06 0.01893  1.14197E-02 0.00045 ];
INF_SP6                   (idx, [1:   8]) = [  7.57073E-03 0.00029 -2.66640E-04 0.00120 -9.47634E-06 0.00523 -3.10080E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.28603E-03 0.00146 -4.71024E-04 0.00063 -1.13506E-05 0.00404  1.06931E-02 0.00040 ];

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

