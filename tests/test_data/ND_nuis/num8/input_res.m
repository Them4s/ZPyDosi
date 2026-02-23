
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
START_DATE                (idx, [1: 24])  = 'Sat Jan 17 22:49:49 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Sun Jan 18 18:34:10 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.24561E+00  1.00063E+00  9.95197E-01  9.99230E-01  1.00126E+00  9.92615E-01  9.96594E-01  9.95589E-01  9.91953E-01  9.94626E-01  9.86520E-01  9.83878E-01  9.93618E-01  9.96276E-01  9.94135E-01  9.90365E-01  9.93908E-01  9.91373E-01  1.00391E+00  9.78661E-01  9.90307E-01  9.83639E-01  9.85558E-01  9.89766E-01  9.84344E-01  9.93267E-01  9.95397E-01  9.79679E-01  9.82009E-01  9.90086E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 1.2E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.79954E-01 9.9E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.44617E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.44521E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.72752E+00 0.00021  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.25116E+02 0.00023  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2130764408 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.55127E+05 0.00051 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.41779E+04 ;
RUNNING_TIME              (idx, 1)        =  1.18436E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.73050E-01  3.73050E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.18333E-03  9.18333E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.18397E+03  1.18397E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.18436E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85780 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88661E+01 2.9E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85683E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.20 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32931E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.20584E-01 9.7E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.35954E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.40463E-02 0.00025 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.31614E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.98343E-01 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.06164E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.75949E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82113E-01 9.7E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98793E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.30285E+01 3.0E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.78869E-02 0.00053 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.01906E+01 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.45798E+00 1.2E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02251E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  9.99630E-01 5.3E-05  9.92173E-01 5.0E-05  7.46257E-03 0.00072 ];
IMP_KEFF                  (idx, [1:   2]) = [  9.99625E-01 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  9.99556E-01 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  9.99625E-01 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01785E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  1.98589E-03 0.00204  5.66546E-05 0.00901  2.86424E-04 0.00442  1.62314E-04 0.00565  3.69764E-04 0.00395  6.41030E-04 0.00308  2.19353E-04 0.00535  1.78350E-04 0.00632  7.20053E-05 0.01006 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.62674E-01 0.00075  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.53713E-03 0.00069  2.24343E-04 0.00402  1.09011E-03 0.00181  6.38111E-04 0.00231  1.41868E-03 0.00158  2.43292E-03 0.00122  8.09148E-04 0.00208  6.70145E-04 0.00228  2.53684E-04 0.00378 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.64057E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.76488E-05 0.00011  4.76263E-05 0.00011  5.06248E-05 0.00098 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.76304E-05 9.2E-05  4.76078E-05 9.2E-05  5.06050E-05 0.00098 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.46320E-03 0.00074  2.21270E-04 0.00430  1.07585E-03 0.00194  6.32615E-04 0.00256  1.40305E-03 0.00173  2.41310E-03 0.00132  8.02007E-04 0.00229  6.62114E-04 0.00251  2.53183E-04 0.00412 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.64852E-01 0.00117  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.69178E-05 0.00022  4.68954E-05 0.00022  4.98251E-05 0.00228 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.68996E-05 0.00021  4.68772E-05 0.00021  4.98060E-05 0.00228 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.57023E-03 0.00217  2.34442E-04 0.01239  1.09134E-03 0.00563  6.45315E-04 0.00726  1.42398E-03 0.00503  2.44582E-03 0.00381  8.14805E-04 0.00659  6.65616E-04 0.00733  2.48919E-04 0.01166 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.59825E-01 0.00330  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.57393E-03 0.00213  2.35069E-04 0.01213  1.09328E-03 0.00554  6.45515E-04 0.00720  1.42287E-03 0.00493  2.44813E-03 0.00373  8.15062E-04 0.00648  6.64075E-04 0.00716  2.49923E-04 0.01155 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.59764E-01 0.00326  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.61470E+02 0.00218 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.72869E-05 6.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.72686E-05 4.1E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.55442E-03 0.00043 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.59762E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.37331E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96081E-06 4.6E-05  1.96065E-06 4.7E-05  1.98193E-06 0.00051 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.16063E-05 7.5E-05  7.16631E-05 7.5E-05  6.41476E-05 0.00084 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02255E-01 2.1E-05 -3.50776E-02 0.00185  2.56076E-04 0.00186 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21801E+01 0.00112 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01778E+00 5.6E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.69998E+01 4.7E-05  1.60289E+01 6.4E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.96815E-01 3.1E-05  2.58140E+00 3.0E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.00882E-03 7.4E-05  2.74951E-02 3.3E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.79087E-03 6.1E-05  4.98330E-02 5.8E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.78205E-03 6.4E-05  2.23379E-02 9.4E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.66169E-03 6.5E-05  5.44320E-02 9.4E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.61591E+00 7.4E-06  2.43676E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04555E+02 7.3E-07  2.01942E+02 7.7E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.37107E-08 5.3E-05  3.57929E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.90015E-01 3.1E-05  2.53157E+00 3.1E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.51386E-01 3.5E-05  5.21813E-01 3.3E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37260E-01 4.0E-05  8.99867E-02 8.9E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.03590E-03 0.00030  2.38407E-02 0.00027 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61171E-02 0.00015 -2.04503E-02 0.00025 ];
INF_SCATT5                (idx, [1:   4]) = [  3.61986E-05 0.06068  1.14090E-02 0.00043 ];
INF_SCATT6                (idx, [1:   4]) = [  7.27475E-03 0.00028 -3.10423E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.11502E-04 0.00223  1.06756E-02 0.00041 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.90071E-01 3.1E-05  2.53157E+00 3.1E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.51389E-01 3.5E-05  5.21813E-01 3.3E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37261E-01 4.0E-05  8.99867E-02 8.9E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.03608E-03 0.00030  2.38407E-02 0.00027 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61170E-02 0.00015 -2.04503E-02 0.00025 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.62300E-05 0.06062  1.14090E-02 0.00043 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.27478E-03 0.00028 -3.10423E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.11548E-04 0.00222  1.06756E-02 0.00041 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.44679E-01 3.9E-05  1.73130E+00 3.8E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.36233E+00 3.9E-05  1.92534E-01 3.8E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.73421E-03 6.1E-05  4.98323E-02 5.8E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.66109E-02 4.3E-05  5.00676E-02 7.2E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  1.34051E-10 0.53367 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 6.6E-10  1.39446E-12 1.00000 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 9.4E-09  1.73264E-08 0.53509 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.60204E-01 3.1E-05  2.98107E-02 4.1E-05  2.29656E-04 0.00069  2.53134E+00 3.1E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.42641E-01 3.5E-05  8.74467E-03 7.9E-05  1.32123E-04 0.00084  5.21681E-01 3.3E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40309E-01 4.0E-05 -3.04927E-03 0.00016  8.35112E-05 0.00102  8.99032E-02 8.9E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24392E-02 0.00022 -3.40326E-03 0.00012  4.28401E-05 0.00167  2.37978E-02 0.00027 ];
INF_S4                    (idx, [1:   8]) = [ -1.53194E-02 0.00015 -7.97678E-04 0.00047  1.37404E-05 0.00419 -2.04640E-02 0.00025 ];
INF_S5                    (idx, [1:   8]) = [ -2.98928E-04 0.00719  3.35127E-04 0.00106 -2.61210E-06 0.01970  1.14116E-02 0.00043 ];
INF_S6                    (idx, [1:   8]) = [  7.54120E-03 0.00027 -2.66459E-04 0.00121 -9.52589E-06 0.00499 -3.10327E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.28123E-03 0.00137 -4.69725E-04 0.00070 -1.13316E-05 0.00377  1.06870E-02 0.00041 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.60261E-01 3.1E-05  2.98107E-02 4.1E-05  2.29656E-04 0.00069  2.53134E+00 3.1E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.42644E-01 3.5E-05  8.74468E-03 7.9E-05  1.32123E-04 0.00084  5.21681E-01 3.3E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40311E-01 4.0E-05 -3.04927E-03 0.00016  8.35112E-05 0.00102  8.99032E-02 8.9E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24393E-02 0.00022 -3.40326E-03 0.00012  4.28401E-05 0.00167  2.37978E-02 0.00027 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53193E-02 0.00015 -7.97678E-04 0.00047  1.37404E-05 0.00419 -2.04640E-02 0.00025 ];
INF_SP5                   (idx, [1:   8]) = [ -2.98897E-04 0.00719  3.35127E-04 0.00106 -2.61210E-06 0.01970  1.14116E-02 0.00043 ];
INF_SP6                   (idx, [1:   8]) = [  7.54124E-03 0.00027 -2.66459E-04 0.00121 -9.52590E-06 0.00499 -3.10327E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.28127E-03 0.00137 -4.69725E-04 0.00070 -1.13316E-05 0.00377  1.06870E-02 0.00041 ];

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

