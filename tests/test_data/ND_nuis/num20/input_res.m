
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
START_DATE                (idx, [1: 24])  = 'Thu Jan 22 20:24:13 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Jan 23 15:51:34 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.23636E+00  1.01164E+00  9.96313E-01  1.00377E+00  9.94637E-01  9.99383E-01  9.84282E-01  9.88360E-01  9.78928E-01  9.78818E-01  9.90540E-01  9.90515E-01  9.87187E-01  1.00111E+00  9.93951E-01  9.96997E-01  9.83269E-01  9.97920E-01  9.87401E-01  9.97419E-01  9.95348E-01  9.87084E-01  9.95887E-01  9.86682E-01  9.97060E-01  9.94162E-01  9.78010E-01  9.86935E-01  9.94649E-01  9.85384E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.80972E-01 9.0E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.55665E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.55573E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.65955E+00 0.00021  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26594E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2073245766 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.45541E+05 0.00052 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.36883E+04 ;
RUNNING_TIME              (idx, 1)        =  1.16735E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.74250E-01  3.74250E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.20000E-03  9.20000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.16696E+03  1.16696E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.16735E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85886 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88667E+01 3.2E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85830E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.26 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32915E-05 3.5E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.12580E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.35323E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.46768E-02 0.00025 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.33827E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.01877E+00 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.12987E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.69538E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82525E-01 9.6E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98746E-01 3.5E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.32173E+01 3.2E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.74753E-02 0.00054 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.07867E+01 5.2E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46684E+00 1.3E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02254E+02 1.5E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.02007E+00 5.4E-05  1.01247E+00 5.1E-05  7.58667E-03 0.00073 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.02006E+00 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.02006E+00 4.6E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.02006E+00 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03823E+00 3.1E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.04686E-03 0.00216  5.75835E-05 0.00894  2.93411E-04 0.00435  1.67309E-04 0.00572  3.80669E-04 0.00400  6.59656E-04 0.00337  2.26625E-04 0.00561  1.87107E-04 0.00607  7.44941E-05 0.01102 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.63505E-01 0.00077  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.50843E-03 0.00069  2.21620E-04 0.00405  1.08086E-03 0.00186  6.36425E-04 0.00244  1.41411E-03 0.00161  2.42192E-03 0.00123  8.08594E-04 0.00218  6.70276E-04 0.00235  2.54631E-04 0.00377 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.65722E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.70335E-05 0.00011  4.70105E-05 0.00011  5.00596E-05 0.00098 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.79765E-05 9.6E-05  4.79531E-05 9.6E-05  5.10632E-05 0.00097 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.43899E-03 0.00075  2.20426E-04 0.00439  1.07164E-03 0.00196  6.28575E-04 0.00261  1.39973E-03 0.00176  2.40446E-03 0.00134  7.97475E-04 0.00237  6.63666E-04 0.00258  2.53019E-04 0.00420 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.65733E-01 0.00121  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.62909E-05 0.00022  4.62679E-05 0.00022  4.93202E-05 0.00228 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.72191E-05 0.00021  4.71956E-05 0.00022  5.03096E-05 0.00228 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.58595E-03 0.00218  2.27739E-04 0.01273  1.08827E-03 0.00569  6.51402E-04 0.00743  1.43408E-03 0.00500  2.45840E-03 0.00382  8.00004E-04 0.00667  6.72013E-04 0.00734  2.54035E-04 0.01180 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.62154E-01 0.00334  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.58790E-03 0.00214  2.27761E-04 0.01252  1.08866E-03 0.00560  6.49898E-04 0.00725  1.43557E-03 0.00490  2.45978E-03 0.00376  8.00680E-04 0.00653  6.72113E-04 0.00718  2.53439E-04 0.01148 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.61893E-01 0.00325  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.64011E+02 0.00220 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.66697E-05 7.0E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.76054E-05 4.4E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.53691E-03 0.00043 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.61499E+02 0.00044 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.39030E-06 5.5E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96061E-06 4.8E-05  1.96047E-06 4.8E-05  1.97909E-06 0.00055 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.28951E-05 7.9E-05  7.29541E-05 7.9E-05  6.51200E-05 0.00090 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.01774E-01 2.2E-05 -3.34445E-02 0.00190  2.43988E-04 0.00190 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21697E+01 0.00112 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.03817E+00 5.4E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.69375E+01 4.6E-05  1.62799E+01 6.6E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.96054E-01 3.1E-05  2.58215E+00 3.1E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.98818E-03 8.0E-05  2.67307E-02 3.4E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.83903E-03 6.5E-05  4.90363E-02 5.9E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.85085E-03 6.6E-05  2.23056E-02 9.5E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.88546E-03 6.7E-05  5.44953E-02 9.5E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.63958E+00 8.1E-06  2.44313E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04530E+02 7.1E-07  2.01942E+02 7.7E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.38191E-08 5.8E-05  3.58519E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.89204E-01 3.1E-05  2.53311E+00 3.2E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.52423E-01 3.5E-05  5.21905E-01 3.5E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37644E-01 4.0E-05  8.98509E-02 9.7E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.08731E-03 0.00029  2.37836E-02 0.00030 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61511E-02 0.00015 -2.05208E-02 0.00029 ];
INF_SCATT5                (idx, [1:   4]) = [  3.14992E-05 0.07197  1.14393E-02 0.00047 ];
INF_SCATT6                (idx, [1:   4]) = [  7.28879E-03 0.00028 -3.11173E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.12245E-04 0.00238  1.07385E-02 0.00045 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.89260E-01 3.1E-05  2.53312E+00 3.2E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.52426E-01 3.5E-05  5.21905E-01 3.5E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37645E-01 4.0E-05  8.98509E-02 9.7E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.08747E-03 0.00029  2.37836E-02 0.00030 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61511E-02 0.00015 -2.05208E-02 0.00029 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.15294E-05 0.07191  1.14393E-02 0.00047 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.28883E-03 0.00028 -3.11173E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.12252E-04 0.00238  1.07385E-02 0.00045 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.44506E-01 4.1E-05  1.73206E+00 3.8E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.36330E+00 4.1E-05  1.92449E-01 3.8E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.78306E-03 6.5E-05  4.90356E-02 5.9E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.67100E-02 4.7E-05  4.92627E-02 7.4E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 6.6E-10  1.02623E-09 0.61179 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 8.5E-08  1.39574E-07 0.61085 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.59344E-01 3.1E-05  2.98600E-02 4.2E-05  2.25467E-04 0.00063  2.53289E+00 3.2E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.43657E-01 3.5E-05  8.76536E-03 8.2E-05  1.30152E-04 0.00088  5.21775E-01 3.5E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40699E-01 4.0E-05 -3.05548E-03 0.00018  8.24347E-05 0.00108  8.97685E-02 9.7E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24984E-02 0.00020 -3.41111E-03 0.00014  4.23536E-05 0.00164  2.37412E-02 0.00030 ];
INF_S4                    (idx, [1:   8]) = [ -1.53514E-02 0.00015 -7.99714E-04 0.00053  1.35804E-05 0.00422 -2.05344E-02 0.00029 ];
INF_S5                    (idx, [1:   8]) = [ -3.04021E-04 0.00731  3.35521E-04 0.00111 -2.54412E-06 0.02127  1.14419E-02 0.00047 ];
INF_S6                    (idx, [1:   8]) = [  7.55569E-03 0.00027 -2.66905E-04 0.00123 -9.35165E-06 0.00526 -3.11080E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.28236E-03 0.00150 -4.70120E-04 0.00072 -1.11693E-05 0.00390  1.07497E-02 0.00045 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.59400E-01 3.1E-05  2.98600E-02 4.2E-05  2.25468E-04 0.00063  2.53289E+00 3.2E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.43660E-01 3.5E-05  8.76536E-03 8.2E-05  1.30152E-04 0.00088  5.21775E-01 3.5E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40701E-01 4.0E-05 -3.05548E-03 0.00018  8.24346E-05 0.00108  8.97685E-02 9.7E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24986E-02 0.00020 -3.41111E-03 0.00014  4.23536E-05 0.00164  2.37412E-02 0.00030 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53514E-02 0.00015 -7.99714E-04 0.00053  1.35804E-05 0.00422 -2.05344E-02 0.00029 ];
INF_SP5                   (idx, [1:   8]) = [ -3.03991E-04 0.00731  3.35521E-04 0.00111 -2.54412E-06 0.02127  1.14419E-02 0.00047 ];
INF_SP6                   (idx, [1:   8]) = [  7.55574E-03 0.00027 -2.66905E-04 0.00123 -9.35165E-06 0.00526 -3.11080E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.28237E-03 0.00150 -4.70120E-04 0.00072 -1.11693E-05 0.00390  1.07497E-02 0.00045 ];

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

