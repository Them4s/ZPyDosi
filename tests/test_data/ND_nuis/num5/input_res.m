
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
START_DATE                (idx, [1: 24])  = 'Sat Jan 17 02:52:54 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Sat Jan 17 22:06:22 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.21559E+00  9.91120E-01  9.98134E-01  9.87637E-01  9.81744E-01  9.94351E-01  9.96776E-01  1.00072E+00  1.00130E+00  9.76073E-01  9.99134E-01  9.82729E-01  9.81516E-01  9.97889E-01  9.95306E-01  9.80649E-01  9.96301E-01  9.84018E-01  9.94345E-01  1.00530E+00  9.95146E-01  9.86640E-01  9.99061E-01  9.95741E-01  9.96928E-01  1.00100E+00  9.94865E-01  9.88164E-01  9.96373E-01  9.85455E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.81021E-01 9.6E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.60014E+01 0.00023  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.59923E+01 0.00023  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.66360E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.27412E+02 0.00025  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2034814112 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.39136E+05 0.00053 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.32937E+04 ;
RUNNING_TIME              (idx, 1)        =  1.15346E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.77883E-01  3.77883E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  8.71667E-03  8.71667E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.15308E+03  1.15308E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.15346E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.86413 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88724E+01 3.1E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85907E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.30 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32923E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.12349E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.38009E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.19911E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32996E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.00661E+00 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.10448E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.72308E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82756E-01 9.4E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98768E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.31591E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.72442E-02 0.00054 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.07727E+01 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.45246E+00 1.4E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02241E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00790E+00 5.4E-05  1.00037E+00 5.1E-05  7.50780E-03 0.00072 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00788E+00 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00786E+00 4.6E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00788E+00 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.02559E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.05261E-03 0.00213  5.93160E-05 0.01132  2.96054E-04 0.00446  1.69460E-04 0.00559  3.80849E-04 0.00394  6.63209E-04 0.00320  2.25206E-04 0.00523  1.84941E-04 0.00545  7.35714E-05 0.00977 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.61323E-01 0.00078  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.52492E-03 0.00069  2.23837E-04 0.00410  1.08407E-03 0.00181  6.41240E-04 0.00243  1.41655E-03 0.00159  2.43322E-03 0.00122  8.05612E-04 0.00211  6.68662E-04 0.00236  2.51728E-04 0.00386 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.63211E-01 0.00109  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.77373E-05 0.00011  4.77155E-05 0.00011  5.06141E-05 0.00097 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.81134E-05 9.4E-05  4.80915E-05 9.4E-05  5.10132E-05 0.00097 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.45050E-03 0.00074  2.20191E-04 0.00438  1.07305E-03 0.00201  6.34352E-04 0.00264  1.40117E-03 0.00174  2.41075E-03 0.00132  7.98248E-04 0.00232  6.62353E-04 0.00255  2.50402E-04 0.00423 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.63953E-01 0.00121  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.69804E-05 0.00022  4.69590E-05 0.00022  4.97658E-05 0.00227 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.73506E-05 0.00021  4.73290E-05 0.00021  5.01590E-05 0.00227 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.58508E-03 0.00216  2.27042E-04 0.01266  1.09745E-03 0.00572  6.50923E-04 0.00743  1.42396E-03 0.00499  2.45267E-03 0.00385  8.11305E-04 0.00673  6.69094E-04 0.00740  2.52645E-04 0.01213 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.61608E-01 0.00340  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.58526E-03 0.00212  2.26539E-04 0.01236  1.09570E-03 0.00559  6.51716E-04 0.00731  1.42479E-03 0.00491  2.45465E-03 0.00377  8.11169E-04 0.00663  6.68166E-04 0.00724  2.52532E-04 0.01190 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.61502E-01 0.00334  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.61576E+02 0.00217 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.73663E-05 6.9E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.77395E-05 4.4E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.56151E-03 0.00042 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.59644E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38861E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96342E-06 4.7E-05  1.96328E-06 4.7E-05  1.98103E-06 0.00052 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.26054E-05 7.6E-05  7.26637E-05 7.7E-05  6.49370E-05 0.00084 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02780E-01 2.2E-05 -3.35793E-02 0.00187  2.45122E-04 0.00189 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21805E+01 0.00112 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.02556E+00 4.9E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.69169E+01 4.4E-05  1.62423E+01 6.5E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  7.01065E-01 2.9E-05  2.57984E+00 3.0E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.03437E-03 8.1E-05  2.68929E-02 3.4E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.81858E-03 6.7E-05  4.92065E-02 5.9E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.78422E-03 6.2E-05  2.23137E-02 9.5E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.73043E-03 6.4E-05  5.41356E-02 9.5E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.65126E+00 7.9E-06  2.42612E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04502E+02 7.0E-07  2.01942E+02 7.8E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.40122E-08 4.9E-05  3.58378E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.94238E-01 2.9E-05  2.53063E+00 3.1E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.53021E-01 3.2E-05  5.21249E-01 3.4E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37836E-01 3.7E-05  8.97839E-02 9.1E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.05557E-03 0.00027  2.37761E-02 0.00030 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61930E-02 0.00015 -2.04812E-02 0.00028 ];
INF_SCATT5                (idx, [1:   4]) = [  1.94775E-05 0.10778  1.14213E-02 0.00047 ];
INF_SCATT6                (idx, [1:   4]) = [  7.28654E-03 0.00028 -3.10574E-02 0.00015 ];
INF_SCATT7                (idx, [1:   4]) = [  8.08471E-04 0.00235  1.06995E-02 0.00042 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.94294E-01 2.9E-05  2.53063E+00 3.1E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.53024E-01 3.2E-05  5.21249E-01 3.4E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37838E-01 3.7E-05  8.97839E-02 9.1E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.05577E-03 0.00027  2.37761E-02 0.00030 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61929E-02 0.00015 -2.04812E-02 0.00028 ];
INF_SCATTP5               (idx, [1:   4]) = [  1.94817E-05 0.10775  1.14213E-02 0.00047 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.28658E-03 0.00028 -3.10574E-02 0.00015 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.08486E-04 0.00235  1.06995E-02 0.00042 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.50048E-01 3.7E-05  1.73114E+00 3.7E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.33308E+00 3.7E-05  1.92552E-01 3.7E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.76265E-03 6.8E-05  4.92059E-02 5.9E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.67484E-02 4.2E-05  4.94368E-02 7.7E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 1.3E-09  1.75444E-09 0.76165 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 6.6E-10  8.71591E-11 0.77693 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 1.7E-07  2.16814E-07 0.79826 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.64317E-01 2.9E-05  2.99214E-02 3.9E-05  2.26955E-04 0.00065  2.53040E+00 3.1E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.44242E-01 3.2E-05  8.77914E-03 8.1E-05  1.30855E-04 0.00084  5.21118E-01 3.4E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40897E-01 3.6E-05 -3.06091E-03 0.00018  8.26682E-05 0.00100  8.97012E-02 9.2E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24724E-02 0.00020 -3.41681E-03 0.00014  4.23796E-05 0.00162  2.37337E-02 0.00030 ];
INF_S4                    (idx, [1:   8]) = [ -1.53914E-02 0.00016 -8.01564E-04 0.00050  1.35284E-05 0.00421 -2.04947E-02 0.00028 ];
INF_S5                    (idx, [1:   8]) = [ -3.16914E-04 0.00661  3.36392E-04 0.00104 -2.64710E-06 0.01908  1.14240E-02 0.00047 ];
INF_S6                    (idx, [1:   8]) = [  7.55342E-03 0.00027 -2.66873E-04 0.00120 -9.45451E-06 0.00522 -3.10479E-02 0.00015 ];
INF_S7                    (idx, [1:   8]) = [  1.27960E-03 0.00144 -4.71127E-04 0.00068 -1.12400E-05 0.00401  1.07107E-02 0.00042 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.64373E-01 2.9E-05  2.99214E-02 3.9E-05  2.26956E-04 0.00065  2.53040E+00 3.1E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.44245E-01 3.2E-05  8.77914E-03 8.1E-05  1.30855E-04 0.00084  5.21118E-01 3.4E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40898E-01 3.6E-05 -3.06091E-03 0.00018  8.26682E-05 0.00100  8.97012E-02 9.2E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24726E-02 0.00020 -3.41682E-03 0.00014  4.23796E-05 0.00162  2.37337E-02 0.00030 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53914E-02 0.00016 -8.01564E-04 0.00050  1.35283E-05 0.00421 -2.04947E-02 0.00028 ];
INF_SP5                   (idx, [1:   8]) = [ -3.16910E-04 0.00661  3.36392E-04 0.00104 -2.64710E-06 0.01908  1.14240E-02 0.00047 ];
INF_SP6                   (idx, [1:   8]) = [  7.55346E-03 0.00027 -2.66874E-04 0.00120 -9.45451E-06 0.00522 -3.10479E-02 0.00015 ];
INF_SP7                   (idx, [1:   8]) = [  1.27961E-03 0.00144 -4.71127E-04 0.00068 -1.12400E-05 0.00401  1.07107E-02 0.00042 ];

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

