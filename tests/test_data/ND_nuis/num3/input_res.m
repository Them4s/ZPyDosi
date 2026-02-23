
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
START_DATE                (idx, [1: 24])  = 'Fri Jan 16 07:31:26 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Sat Jan 17 02:52:52 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.22505E+00  9.98355E-01  1.01399E+00  9.95374E-01  9.93890E-01  9.87005E-01  9.93315E-01  9.84886E-01  9.92444E-01  1.00103E+00  9.91917E-01  9.94798E-01  9.84564E-01  9.96580E-01  9.89176E-01  9.96142E-01  9.94550E-01  9.92439E-01  9.97124E-01  9.90517E-01  9.86509E-01  9.87102E-01  9.84276E-01  9.89972E-01  9.93275E-01  9.95811E-01  9.92337E-01  9.85118E-01  9.84576E-01  9.87890E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 1.0E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.80946E-01 9.4E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.61135E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.61043E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.67250E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26219E+02 0.00025  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2058769081 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.43128E+05 0.00052 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.35142E+04 ;
RUNNING_TIME              (idx, 1)        =  1.16144E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.76450E-01  3.76450E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.36667E-03  9.36667E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.16106E+03  1.16106E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.16144E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85568 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88640E+01 3.1E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85553E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.14 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32917E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.16756E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.41174E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  5.88255E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.33085E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.99308E-01 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.10754E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.71924E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82678E-01 9.2E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98752E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.32050E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.73219E-02 0.00052 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.11242E+01 5.3E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.43286E+00 1.2E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02226E+02 1.3E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00065E+00 5.2E-05  9.93124E-01 4.9E-05  7.50122E-03 0.00073 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00057E+00 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00056E+00 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00057E+00 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01823E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.06756E-03 0.00194  5.85427E-05 0.00824  3.00155E-04 0.00409  1.71862E-04 0.00543  3.87275E-04 0.00372  6.65463E-04 0.00302  2.24279E-04 0.00493  1.86619E-04 0.00555  7.33660E-05 0.00883 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.58806E-01 0.00077  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.56206E-03 0.00068  2.25219E-04 0.00400  1.09425E-03 0.00182  6.45262E-04 0.00239  1.42911E-03 0.00159  2.44385E-03 0.00124  8.04396E-04 0.00213  6.69148E-04 0.00232  2.50837E-04 0.00386 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.61185E-01 0.00109  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.83063E-05 0.00011  4.82859E-05 0.00011  5.09734E-05 0.00098 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.83371E-05 9.3E-05  4.83168E-05 9.3E-05  5.10063E-05 0.00098 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.49691E-03 0.00075  2.23320E-04 0.00436  1.08497E-03 0.00198  6.39246E-04 0.00258  1.41786E-03 0.00172  2.42176E-03 0.00133  7.96992E-04 0.00232  6.63954E-04 0.00256  2.48804E-04 0.00415 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.61348E-01 0.00119  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.74989E-05 0.00022  4.74781E-05 0.00022  5.01947E-05 0.00219 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.75292E-05 0.00021  4.75084E-05 0.00021  5.02270E-05 0.00219 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.62752E-03 0.00217  2.28926E-04 0.01255  1.10678E-03 0.00569  6.55353E-04 0.00733  1.45897E-03 0.00501  2.45822E-03 0.00381  8.09540E-04 0.00671  6.61135E-04 0.00732  2.48605E-04 0.01220 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.56077E-01 0.00339  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.62821E-03 0.00212  2.29149E-04 0.01223  1.10809E-03 0.00556  6.56451E-04 0.00721  1.45807E-03 0.00489  2.45718E-03 0.00372  8.09770E-04 0.00660  6.61381E-04 0.00722  2.48115E-04 0.01196 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.55794E-01 0.00334  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.60700E+02 0.00218 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.79086E-05 6.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.79392E-05 4.3E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.60239E-03 0.00043 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.58689E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.39810E-06 5.4E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96016E-06 4.8E-05  1.96002E-06 4.8E-05  1.97865E-06 0.00054 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.30732E-05 7.9E-05  7.31328E-05 7.9E-05  6.52399E-05 0.00088 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.04126E-01 2.2E-05 -3.32503E-02 0.00178  2.43230E-04 0.00179 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.22119E+01 0.00112 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01825E+00 5.6E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.68417E+01 4.4E-05  1.63635E+01 7.3E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  7.01922E-01 2.9E-05  2.58404E+00 3.2E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.02725E-03 8.4E-05  2.67051E-02 3.7E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.78300E-03 6.9E-05  4.89272E-02 6.6E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.75576E-03 6.6E-05  2.22221E-02 0.00010 ];
INF_NSF                   (idx, [1:   4]) = [  4.57678E-03 6.7E-05  5.35625E-02 0.00010 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.60673E+00 7.7E-06  2.41033E+00 9.3E-10 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04420E+02 6.8E-07  2.01942E+02 7.6E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.42206E-08 5.1E-05  3.58615E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.95131E-01 2.9E-05  2.53511E+00 3.4E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.54323E-01 3.3E-05  5.22115E-01 3.4E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.38283E-01 3.9E-05  8.98453E-02 8.7E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.01309E-03 0.00030  2.37872E-02 0.00028 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.63265E-02 0.00015 -2.05398E-02 0.00029 ];
INF_SCATT5                (idx, [1:   4]) = [ -2.06771E-06 1.00000  1.14546E-02 0.00042 ];
INF_SCATT6                (idx, [1:   4]) = [  7.31563E-03 0.00027 -3.11343E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.08649E-04 0.00213  1.07463E-02 0.00046 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.95187E-01 2.9E-05  2.53511E+00 3.4E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.54326E-01 3.3E-05  5.22115E-01 3.4E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.38284E-01 3.9E-05  8.98453E-02 8.7E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.01324E-03 0.00030  2.37872E-02 0.00028 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.63265E-02 0.00015 -2.05398E-02 0.00029 ];
INF_SCATTP5               (idx, [1:   4]) = [ -2.07329E-06 1.00000  1.14546E-02 0.00042 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.31566E-03 0.00027 -3.11343E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.08668E-04 0.00213  1.07463E-02 0.00046 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.48697E-01 4.0E-05  1.73352E+00 3.9E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.34032E+00 4.0E-05  1.92287E-01 3.9E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.72709E-03 7.0E-05  4.89265E-02 6.6E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.68456E-02 4.3E-05  4.91540E-02 8.1E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 7.3E-09  8.10300E-09 0.91165 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 6.6E-10  4.23810E-10 1.00000 ];
INF_CHID                  (idx, [1:   4]) = [  9.99999E-01 9.7E-07  1.00998E-06 0.95964 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.65077E-01 2.9E-05  3.00548E-02 3.9E-05  2.25219E-04 0.00067  2.53488E+00 3.4E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.45503E-01 3.3E-05  8.82053E-03 7.6E-05  1.29973E-04 0.00087  5.21985E-01 3.4E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.41358E-01 3.9E-05 -3.07548E-03 0.00018  8.22938E-05 0.00108  8.97630E-02 8.7E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24453E-02 0.00022 -3.43223E-03 0.00014  4.22282E-05 0.00154  2.37449E-02 0.00028 ];
INF_S4                    (idx, [1:   8]) = [ -1.55221E-02 0.00016 -8.04421E-04 0.00048  1.35448E-05 0.00429 -2.05533E-02 0.00029 ];
INF_S5                    (idx, [1:   8]) = [ -3.40125E-04 0.00621  3.38057E-04 0.00104 -2.53233E-06 0.02078  1.14571E-02 0.00042 ];
INF_S6                    (idx, [1:   8]) = [  7.58376E-03 0.00026 -2.68128E-04 0.00125 -9.43095E-06 0.00544 -3.11249E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.28222E-03 0.00131 -4.73568E-04 0.00067 -1.12088E-05 0.00433  1.07575E-02 0.00046 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.65132E-01 2.9E-05  3.00548E-02 3.9E-05  2.25219E-04 0.00067  2.53488E+00 3.4E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.45505E-01 3.3E-05  8.82053E-03 7.6E-05  1.29973E-04 0.00087  5.21985E-01 3.4E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.41360E-01 3.9E-05 -3.07548E-03 0.00018  8.22938E-05 0.00108  8.97630E-02 8.7E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24455E-02 0.00022 -3.43223E-03 0.00014  4.22282E-05 0.00154  2.37450E-02 0.00028 ];
INF_SP4                   (idx, [1:   8]) = [ -1.55221E-02 0.00016 -8.04421E-04 0.00048  1.35448E-05 0.00429 -2.05533E-02 0.00029 ];
INF_SP5                   (idx, [1:   8]) = [ -3.40131E-04 0.00621  3.38057E-04 0.00104 -2.53233E-06 0.02078  1.14571E-02 0.00042 ];
INF_SP6                   (idx, [1:   8]) = [  7.58379E-03 0.00026 -2.68128E-04 0.00125 -9.43095E-06 0.00544 -3.11249E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.28224E-03 0.00131 -4.73568E-04 0.00067 -1.12088E-05 0.00433  1.07575E-02 0.00046 ];

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

