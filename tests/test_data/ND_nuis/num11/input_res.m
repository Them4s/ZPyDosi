
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
START_DATE                (idx, [1: 24])  = 'Mon Jan 19 12:51:09 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Tue Jan 20 09:10:28 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.20383E+00  1.00129E+00  9.86297E-01  9.96329E-01  9.95474E-01  9.91632E-01  9.94967E-01  9.96870E-01  9.86573E-01  9.90641E-01  9.90821E-01  9.93959E-01  9.86022E-01  9.96214E-01  9.91150E-01  9.82592E-01  9.93703E-01  9.90258E-01  9.96787E-01  1.00037E+00  9.97139E-01  9.91560E-01  9.99272E-01  9.98052E-01  9.92997E-01  9.94149E-01  1.00042E+00  9.84771E-01  9.82994E-01  9.92863E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 1.9E-09  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.80514E-01 9.4E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.62523E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.62425E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.71388E+00 0.00021  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26380E+02 0.00023  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2155975072 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.59329E+05 0.00049 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00007 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.51963E+04 ;
RUNNING_TIME              (idx, 1)        =  1.21932E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.73617E-01  3.73617E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.35000E-03  9.35000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.21894E+03  1.21894E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.21932E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.86543 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88729E+01 3.0E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85877E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.28 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32920E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.14842E-01 9.7E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.37983E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.20171E-02 0.00025 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.33322E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.98936E-01 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.11455E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.70540E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.81995E-01 9.5E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98761E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.36873E+01 3.0E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.80054E-02 0.00052 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.15957E+01 5.1E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.42782E+00 1.3E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02241E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00018E+00 5.2E-05  9.92638E-01 4.9E-05  7.55720E-03 0.00071 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00022E+00 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00018E+00 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00022E+00 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01859E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.00566E-03 0.00203  5.64498E-05 0.00898  2.89528E-04 0.00424  1.65688E-04 0.00595  3.74043E-04 0.00386  6.48096E-04 0.00316  2.19062E-04 0.00516  1.80922E-04 0.00591  7.18665E-05 0.00918 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.61517E-01 0.00076  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.63173E-03 0.00067  2.27538E-04 0.00394  1.10104E-03 0.00176  6.47728E-04 0.00231  1.44009E-03 0.00157  2.46707E-03 0.00119  8.15054E-04 0.00209  6.77661E-04 0.00230  2.55546E-04 0.00373 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.63047E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.83046E-05 0.00011  4.82819E-05 0.00011  5.12504E-05 0.00098 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.83126E-05 9.2E-05  4.82899E-05 9.2E-05  5.12587E-05 0.00098 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.55804E-03 0.00073  2.25439E-04 0.00427  1.09065E-03 0.00190  6.41748E-04 0.00250  1.42699E-03 0.00170  2.44283E-03 0.00129  8.06756E-04 0.00225  6.70196E-04 0.00252  2.53433E-04 0.00409 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.62965E-01 0.00117  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.75393E-05 0.00021  4.75163E-05 0.00021  5.05037E-05 0.00216 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.75472E-05 0.00021  4.75242E-05 0.00021  5.05122E-05 0.00216 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.70880E-03 0.00212  2.33811E-04 0.01216  1.11156E-03 0.00556  6.60735E-04 0.00719  1.45455E-03 0.00475  2.49361E-03 0.00370  8.21827E-04 0.00656  6.79282E-04 0.00703  2.53429E-04 0.01182 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.59556E-01 0.00328  1.24667E-02 4.9E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.70737E-03 0.00208  2.34050E-04 0.01184  1.11123E-03 0.00542  6.60626E-04 0.00713  1.45153E-03 0.00464  2.49482E-03 0.00362  8.21587E-04 0.00644  6.80324E-04 0.00691  2.53202E-04 0.01152 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.59798E-01 0.00321  1.24667E-02 4.9E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.62278E+02 0.00213 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.79249E-05 6.6E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.79328E-05 4.0E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.67265E-03 0.00041 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.60102E+02 0.00042 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.39407E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96264E-06 4.8E-05  1.96248E-06 4.8E-05  1.98394E-06 0.00053 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.38234E-05 7.7E-05  7.38871E-05 7.7E-05  6.55283E-05 0.00087 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02746E-01 2.1E-05 -3.42602E-02 0.00185  2.52718E-04 0.00186 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21759E+01 0.00110 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01854E+00 5.1E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.72037E+01 4.3E-05  1.64838E+01 6.6E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.93445E-01 2.6E-05  2.59235E+00 3.1E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.96666E-03 7.1E-05  2.64158E-02 3.5E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.72017E-03 5.8E-05  4.84832E-02 5.9E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.75351E-03 5.8E-05  2.20675E-02 9.4E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.60462E-03 6.0E-05  5.30023E-02 9.4E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.62595E+00 7.9E-06  2.40183E+00 2.3E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04527E+02 7.2E-07  2.01942E+02 7.7E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.33110E-08 5.3E-05  3.59029E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.86715E-01 2.7E-05  2.54387E+00 3.2E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.49397E-01 3.0E-05  5.23260E-01 3.4E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.36569E-01 3.6E-05  8.99214E-02 8.4E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.08092E-03 0.00031  2.37969E-02 0.00029 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.59482E-02 0.00015 -2.06146E-02 0.00027 ];
INF_SCATT5                (idx, [1:   4]) = [  6.38754E-05 0.03150  1.14934E-02 0.00043 ];
INF_SCATT6                (idx, [1:   4]) = [  7.23834E-03 0.00026 -3.12510E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.10519E-04 0.00226  1.07983E-02 0.00039 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.86772E-01 2.7E-05  2.54387E+00 3.2E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.49400E-01 3.0E-05  5.23260E-01 3.4E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.36570E-01 3.6E-05  8.99214E-02 8.4E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.08112E-03 0.00031  2.37969E-02 0.00029 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.59482E-02 0.00015 -2.06146E-02 0.00027 ];
INF_SCATTP5               (idx, [1:   4]) = [  6.38919E-05 0.03148  1.14934E-02 0.00043 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.23839E-03 0.00026 -3.12510E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.10537E-04 0.00226  1.07983E-02 0.00039 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.41569E-01 3.7E-05  1.74071E+00 3.7E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.37987E+00 3.7E-05  1.91493E-01 3.7E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.66365E-03 5.8E-05  4.84825E-02 5.9E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.63342E-02 4.1E-05  4.87102E-02 7.6E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 6.6E-10  1.50358E-09 0.59930 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 1.2E-07  1.95294E-07 0.59609 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.57110E-01 2.6E-05  2.96047E-02 3.7E-05  2.23841E-04 0.00067  2.54364E+00 3.2E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.40711E-01 3.0E-05  8.68518E-03 7.2E-05  1.28809E-04 0.00088  5.23131E-01 3.4E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.39597E-01 3.6E-05 -3.02806E-03 0.00018  8.14954E-05 0.00114  8.98399E-02 8.5E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24613E-02 0.00022 -3.38042E-03 0.00013  4.18389E-05 0.00179  2.37551E-02 0.00029 ];
INF_S4                    (idx, [1:   8]) = [ -1.51553E-02 0.00016 -7.92976E-04 0.00049  1.33721E-05 0.00443 -2.06279E-02 0.00027 ];
INF_S5                    (idx, [1:   8]) = [ -2.68526E-04 0.00736  3.32401E-04 0.00105 -2.59563E-06 0.02033  1.14960E-02 0.00043 ];
INF_S6                    (idx, [1:   8]) = [  7.50297E-03 0.00025 -2.64624E-04 0.00117 -9.34906E-06 0.00501 -3.12417E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.27687E-03 0.00142 -4.66353E-04 0.00065 -1.11248E-05 0.00403  1.08094E-02 0.00039 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.57167E-01 2.6E-05  2.96047E-02 3.7E-05  2.23841E-04 0.00067  2.54365E+00 3.2E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.40714E-01 3.0E-05  8.68518E-03 7.2E-05  1.28809E-04 0.00088  5.23131E-01 3.4E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.39598E-01 3.6E-05 -3.02806E-03 0.00018  8.14954E-05 0.00114  8.98399E-02 8.5E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24615E-02 0.00022 -3.38042E-03 0.00013  4.18389E-05 0.00179  2.37551E-02 0.00029 ];
INF_SP4                   (idx, [1:   8]) = [ -1.51552E-02 0.00015 -7.92976E-04 0.00049  1.33721E-05 0.00443 -2.06279E-02 0.00027 ];
INF_SP5                   (idx, [1:   8]) = [ -2.68509E-04 0.00735  3.32401E-04 0.00105 -2.59565E-06 0.02033  1.14960E-02 0.00043 ];
INF_SP6                   (idx, [1:   8]) = [  7.50301E-03 0.00025 -2.64624E-04 0.00117 -9.34906E-06 0.00501 -3.12417E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.27689E-03 0.00142 -4.66353E-04 0.00065 -1.11248E-05 0.00403  1.08094E-02 0.00039 ];

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

