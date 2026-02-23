
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
START_DATE                (idx, [1: 24])  = 'Sat Jan 17 03:17:40 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Sat Jan 17 22:49:47 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.24637E+00  1.00357E+00  9.76828E-01  9.98170E-01  9.85007E-01  9.93701E-01  9.93132E-01  9.91805E-01  9.79315E-01  9.92916E-01  9.97593E-01  9.90227E-01  9.93183E-01  9.85808E-01  9.96044E-01  1.00269E+00  9.88736E-01  1.00115E+00  9.92411E-01  9.94227E-01  9.92954E-01  9.86604E-01  9.94308E-01  9.93534E-01  9.84529E-01  9.90117E-01  9.93927E-01  9.86668E-01  9.79912E-01  9.94557E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.80532E-01 9.2E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.43719E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.43627E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.67496E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.25676E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2107207050 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.51201E+05 0.00051 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00006E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.38128E+04 ;
RUNNING_TIME              (idx, 1)        =  1.17211E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.73483E-01  3.73483E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.45000E-03  9.45000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.17173E+03  1.17173E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.17211E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.84777 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88558E+01 3.2E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85701E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.21 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32905E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.14691E-01 9.9E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.39785E-01 1.6E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.02149E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.31442E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.92215E-01 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.05669E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.76859E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82528E-01 9.1E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98716E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.29661E+01 3.0E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.74719E-02 0.00051 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.01836E+01 4.9E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44587E+00 1.3E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02232E+02 1.3E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  9.93449E-01 5.4E-05  9.86027E-01 5.1E-05  7.42504E-03 0.00072 ];
IMP_KEFF                  (idx, [1:   2]) = [  9.93480E-01 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  9.93498E-01 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  9.93480E-01 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01117E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.00203E-03 0.00187  5.65843E-05 0.00829  2.89676E-04 0.00399  1.66839E-04 0.00516  3.72872E-04 0.00351  6.47068E-04 0.00296  2.17809E-04 0.00471  1.79976E-04 0.00519  7.12033E-05 0.00881 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.60221E-01 0.00076  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.54998E-03 0.00069  2.23736E-04 0.00402  1.09530E-03 0.00182  6.42500E-04 0.00237  1.42330E-03 0.00160  2.43953E-03 0.00121  8.04150E-04 0.00214  6.69756E-04 0.00228  2.51712E-04 0.00383 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.62198E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.82534E-05 0.00011  4.82321E-05 0.00011  5.10515E-05 0.00097 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.79364E-05 9.1E-05  4.79153E-05 9.2E-05  5.07163E-05 0.00097 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.47394E-03 0.00074  2.20696E-04 0.00427  1.08157E-03 0.00197  6.39228E-04 0.00262  1.40917E-03 0.00171  2.41465E-03 0.00132  7.96126E-04 0.00233  6.63553E-04 0.00250  2.48944E-04 0.00414 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.62223E-01 0.00117  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.75494E-05 0.00022  4.75270E-05 0.00022  5.04727E-05 0.00223 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.72372E-05 0.00021  4.72149E-05 0.00021  5.01405E-05 0.00222 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.59480E-03 0.00213  2.34287E-04 0.01236  1.09468E-03 0.00554  6.57050E-04 0.00746  1.43505E-03 0.00496  2.44411E-03 0.00386  8.04325E-04 0.00656  6.74408E-04 0.00718  2.50898E-04 0.01199 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.60673E-01 0.00334  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.59954E-03 0.00210  2.34399E-04 0.01208  1.09577E-03 0.00546  6.57379E-04 0.00732  1.43604E-03 0.00486  2.44617E-03 0.00377  8.05252E-04 0.00641  6.73937E-04 0.00705  2.50590E-04 0.01168 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.60264E-01 0.00327  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.59836E+02 0.00214 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.79184E-05 6.8E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.76037E-05 4.2E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.58047E-03 0.00041 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.58199E+02 0.00042 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.37549E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.95990E-06 4.7E-05  1.95976E-06 4.7E-05  1.97928E-06 0.00052 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.14412E-05 7.5E-05  7.14986E-05 7.5E-05  6.38871E-05 0.00082 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.04251E-01 2.1E-05 -3.47935E-02 0.00173  2.53584E-04 0.00173 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.22043E+01 0.00110 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01121E+00 5.6E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.69290E+01 4.4E-05  1.60373E+01 6.5E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  7.01197E-01 2.8E-05  2.57534E+00 3.0E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.00732E-03 7.7E-05  2.75621E-02 3.5E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.74935E-03 6.4E-05  4.99325E-02 6.1E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.74202E-03 5.9E-05  2.23705E-02 9.9E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.60026E-03 6.1E-05  5.41453E-02 9.9E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.64075E+00 7.6E-06  2.42039E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04458E+02 7.0E-07  2.01942E+02 7.5E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.39767E-08 4.6E-05  3.57775E-06 1.3E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.94439E-01 2.8E-05  2.52541E+00 3.2E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.53394E-01 3.2E-05  5.20381E-01 3.3E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.38026E-01 3.7E-05  8.97797E-02 8.8E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.07915E-03 0.00030  2.37768E-02 0.00027 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.62105E-02 0.00016 -2.03854E-02 0.00029 ];
INF_SCATT5                (idx, [1:   4]) = [  3.23287E-05 0.06599  1.13613E-02 0.00047 ];
INF_SCATT6                (idx, [1:   4]) = [  7.31285E-03 0.00030 -3.09393E-02 0.00015 ];
INF_SCATT7                (idx, [1:   4]) = [  8.16668E-04 0.00241  1.06300E-02 0.00039 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.94495E-01 2.8E-05  2.52541E+00 3.2E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.53397E-01 3.2E-05  5.20381E-01 3.3E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.38027E-01 3.7E-05  8.97797E-02 8.8E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.07933E-03 0.00030  2.37768E-02 0.00027 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.62105E-02 0.00016 -2.03854E-02 0.00029 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.23392E-05 0.06593  1.13613E-02 0.00047 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.31288E-03 0.00030 -3.09393E-02 0.00015 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.16667E-04 0.00241  1.06300E-02 0.00039 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.45980E-01 3.8E-05  1.72836E+00 3.6E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.35512E+00 3.8E-05  1.92861E-01 3.6E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.69314E-03 6.6E-05  4.99319E-02 6.1E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.67200E-02 4.3E-05  5.01627E-02 7.4E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 6.6E-10  6.51190E-10 0.78531 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  3.38066E-11 1.00000 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 6.8E-08  8.21317E-08 0.82731 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.64477E-01 2.8E-05  2.99620E-02 3.9E-05  2.31536E-04 0.00065  2.52518E+00 3.2E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.44609E-01 3.2E-05  8.78506E-03 8.0E-05  1.32957E-04 0.00086  5.20248E-01 3.3E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.41090E-01 3.7E-05 -3.06438E-03 0.00017  8.39604E-05 0.00107  8.96957E-02 8.8E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24988E-02 0.00022 -3.41961E-03 0.00013  4.31057E-05 0.00157  2.37337E-02 0.00027 ];
INF_S4                    (idx, [1:   8]) = [ -1.54087E-02 0.00017 -8.01869E-04 0.00049  1.38334E-05 0.00436 -2.03992E-02 0.00029 ];
INF_S5                    (idx, [1:   8]) = [ -3.04160E-04 0.00700  3.36489E-04 0.00107 -2.52238E-06 0.02201  1.13639E-02 0.00047 ];
INF_S6                    (idx, [1:   8]) = [  7.58042E-03 0.00028 -2.67565E-04 0.00126 -9.49254E-06 0.00492 -3.09298E-02 0.00015 ];
INF_S7                    (idx, [1:   8]) = [  1.28875E-03 0.00151 -4.72084E-04 0.00065 -1.13875E-05 0.00381  1.06414E-02 0.00039 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.64533E-01 2.8E-05  2.99620E-02 3.9E-05  2.31537E-04 0.00065  2.52518E+00 3.2E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.44611E-01 3.2E-05  8.78507E-03 8.0E-05  1.32957E-04 0.00086  5.20248E-01 3.3E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.41092E-01 3.7E-05 -3.06438E-03 0.00017  8.39604E-05 0.00107  8.96957E-02 8.8E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24989E-02 0.00022 -3.41961E-03 0.00013  4.31057E-05 0.00157  2.37337E-02 0.00027 ];
INF_SP4                   (idx, [1:   8]) = [ -1.54086E-02 0.00017 -8.01869E-04 0.00049  1.38334E-05 0.00436 -2.03992E-02 0.00029 ];
INF_SP5                   (idx, [1:   8]) = [ -3.04150E-04 0.00700  3.36489E-04 0.00107 -2.52238E-06 0.02201  1.13639E-02 0.00047 ];
INF_SP6                   (idx, [1:   8]) = [  7.58045E-03 0.00028 -2.67565E-04 0.00126 -9.49254E-06 0.00492 -3.09298E-02 0.00015 ];
INF_SP7                   (idx, [1:   8]) = [  1.28875E-03 0.00151 -4.72084E-04 0.00065 -1.13875E-05 0.00381  1.06414E-02 0.00039 ];

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

