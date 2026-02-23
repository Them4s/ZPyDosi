
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
START_DATE                (idx, [1: 24])  = 'Mon Jan 26 22:13:43 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Tue Jan 27 17:42:45 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.21487E+00  1.00236E+00  9.96835E-01  1.00126E+00  9.90615E-01  9.75867E-01  9.92531E-01  9.87027E-01  9.90886E-01  9.98738E-01  9.77193E-01  9.89699E-01  9.96592E-01  9.90637E-01  9.92113E-01  9.93193E-01  9.85397E-01  9.92945E-01  9.93773E-01  9.96331E-01  9.98485E-01  9.87045E-01  1.00057E+00  1.00393E+00  9.97244E-01  9.87785E-01  9.93577E-01  9.90858E-01  9.85024E-01  9.96617E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.80692E-01 9.8E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.53818E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.53727E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.68080E+00 0.00021  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26403E+02 0.00025  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2086130175 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.47688E+05 0.00052 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00007 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.37346E+04 ;
RUNNING_TIME              (idx, 1)        =  1.16903E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.70683E-01  3.70683E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.48333E-03  9.48333E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.16865E+03  1.16865E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.16902E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85705 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88650E+01 3.0E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85715E-01 ;
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

NORM_COEF                 (idx, [1:   4]) = [  3.32898E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.09391E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.39935E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.00650E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32293E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.00453E+00 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.08298E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.74152E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82449E-01 9.5E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98694E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.31893E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75505E-02 0.00053 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.07502E+01 5.1E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46029E+00 1.3E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02232E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00579E+00 5.2E-05  9.98355E-01 5.0E-05  7.46012E-03 0.00075 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00582E+00 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00585E+00 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00582E+00 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.02381E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.03824E-03 0.00217  5.87079E-05 0.00934  2.94815E-04 0.00472  1.69120E-04 0.00618  3.80041E-04 0.00403  6.57139E-04 0.00324  2.23758E-04 0.00548  1.83298E-04 0.00599  7.13606E-05 0.00960 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.59303E-01 0.00077  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.49391E-03 0.00070  2.23640E-04 0.00413  1.08422E-03 0.00184  6.39689E-04 0.00241  1.41013E-03 0.00162  2.42307E-03 0.00123  8.00288E-04 0.00216  6.63451E-04 0.00233  2.49419E-04 0.00387 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.61926E-01 0.00109  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.79843E-05 0.00011  4.79627E-05 0.00011  5.08428E-05 0.00100 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.82613E-05 9.3E-05  4.82396E-05 9.3E-05  5.11367E-05 0.00100 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.41690E-03 0.00076  2.21092E-04 0.00450  1.07418E-03 0.00197  6.31425E-04 0.00257  1.40007E-03 0.00174  2.39627E-03 0.00134  7.91897E-04 0.00236  6.55827E-04 0.00256  2.46142E-04 0.00418 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.61385E-01 0.00119  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.72424E-05 0.00021  4.72200E-05 0.00022  5.01677E-05 0.00230 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.75152E-05 0.00021  4.74927E-05 0.00021  5.04570E-05 0.00230 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.55538E-03 0.00219  2.27621E-04 0.01271  1.09660E-03 0.00576  6.51340E-04 0.00742  1.44693E-03 0.00494  2.43046E-03 0.00379  7.90926E-04 0.00669  6.64848E-04 0.00738  2.46660E-04 0.01207 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.57403E-01 0.00340  1.24667E-02 5.2E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.55488E-03 0.00214  2.29394E-04 0.01250  1.09508E-03 0.00563  6.51941E-04 0.00731  1.44451E-03 0.00485  2.43185E-03 0.00373  7.92437E-04 0.00658  6.63353E-04 0.00722  2.46324E-04 0.01193 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.57080E-01 0.00334  1.24667E-02 5.2E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.60059E+02 0.00221 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.76180E-05 6.6E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.78929E-05 4.1E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.52339E-03 0.00041 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.57999E+02 0.00042 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38701E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96085E-06 4.9E-05  1.96070E-06 4.9E-05  1.98118E-06 0.00056 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.24268E-05 7.6E-05  7.24849E-05 7.6E-05  6.47193E-05 0.00087 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.04430E-01 2.1E-05 -3.41109E-02 0.00190  2.47017E-04 0.00191 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.22334E+01 0.00115 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.02385E+00 5.5E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.69503E+01 4.4E-05  1.62392E+01 7.0E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.99692E-01 2.8E-05  2.57979E+00 3.0E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.99340E-03 8.1E-05  2.70693E-02 3.8E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.73688E-03 6.6E-05  4.93188E-02 6.5E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.74348E-03 6.0E-05  2.22495E-02 0.00010 ];
INF_NSF                   (idx, [1:   4]) = [  4.62138E-03 6.2E-05  5.41895E-02 0.00010 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.65066E+00 7.8E-06  2.43553E+00 1.6E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04464E+02 7.4E-07  2.01942E+02 7.7E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.39668E-08 5.4E-05  3.58275E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.92946E-01 2.8E-05  2.53048E+00 3.1E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.53196E-01 3.1E-05  5.21097E-01 3.2E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37953E-01 3.7E-05  8.97809E-02 8.9E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.08605E-03 0.00031  2.37719E-02 0.00028 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.62013E-02 0.00015 -2.04670E-02 0.00030 ];
INF_SCATT5                (idx, [1:   4]) = [  2.45252E-05 0.09424  1.14083E-02 0.00046 ];
INF_SCATT6                (idx, [1:   4]) = [  7.30259E-03 0.00027 -3.10242E-02 0.00015 ];
INF_SCATT7                (idx, [1:   4]) = [  8.12902E-04 0.00223  1.06869E-02 0.00041 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.93002E-01 2.8E-05  2.53048E+00 3.1E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.53199E-01 3.1E-05  5.21097E-01 3.2E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37955E-01 3.7E-05  8.97809E-02 8.9E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.08624E-03 0.00031  2.37719E-02 0.00028 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.62012E-02 0.00015 -2.04670E-02 0.00030 ];
INF_SCATTP5               (idx, [1:   4]) = [  2.45482E-05 0.09421  1.14083E-02 0.00046 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.30263E-03 0.00027 -3.10242E-02 0.00015 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.12907E-04 0.00223  1.06869E-02 0.00041 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.45875E-01 3.9E-05  1.73178E+00 3.7E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.35570E+00 3.9E-05  1.92480E-01 3.7E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.68045E-03 6.8E-05  4.93182E-02 6.5E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.66893E-02 4.6E-05  4.95456E-02 7.8E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  1.77236E-10 0.69548 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 1.8E-08  2.50410E-08 0.70013 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.63002E-01 2.7E-05  2.99439E-02 4.1E-05  2.27887E-04 0.00070  2.53025E+00 3.1E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.44414E-01 3.1E-05  8.78191E-03 7.4E-05  1.31052E-04 0.00091  5.20966E-01 3.2E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.41016E-01 3.6E-05 -3.06294E-03 0.00017  8.27394E-05 0.00112  8.96982E-02 8.9E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.25046E-02 0.00023 -3.41855E-03 0.00013  4.24012E-05 0.00164  2.37295E-02 0.00028 ];
INF_S4                    (idx, [1:   8]) = [ -1.53993E-02 0.00016 -8.01979E-04 0.00051  1.35664E-05 0.00437 -2.04806E-02 0.00030 ];
INF_S5                    (idx, [1:   8]) = [ -3.12248E-04 0.00725  3.36773E-04 0.00105 -2.54368E-06 0.01931  1.14108E-02 0.00046 ];
INF_S6                    (idx, [1:   8]) = [  7.56951E-03 0.00026 -2.66919E-04 0.00120 -9.41018E-06 0.00488 -3.10148E-02 0.00015 ];
INF_S7                    (idx, [1:   8]) = [  1.28410E-03 0.00141 -4.71201E-04 0.00063 -1.12015E-05 0.00407  1.06981E-02 0.00041 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.63059E-01 2.7E-05  2.99439E-02 4.1E-05  2.27887E-04 0.00070  2.53025E+00 3.1E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.44417E-01 3.1E-05  8.78191E-03 7.4E-05  1.31052E-04 0.00091  5.20966E-01 3.2E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.41018E-01 3.6E-05 -3.06294E-03 0.00017  8.27394E-05 0.00112  8.96982E-02 8.9E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.25048E-02 0.00023 -3.41855E-03 0.00013  4.24012E-05 0.00164  2.37295E-02 0.00028 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53993E-02 0.00016 -8.01979E-04 0.00051  1.35665E-05 0.00437 -2.04806E-02 0.00030 ];
INF_SP5                   (idx, [1:   8]) = [ -3.12225E-04 0.00726  3.36774E-04 0.00105 -2.54369E-06 0.01931  1.14108E-02 0.00046 ];
INF_SP6                   (idx, [1:   8]) = [  7.56954E-03 0.00026 -2.66919E-04 0.00120 -9.41018E-06 0.00488 -3.10148E-02 0.00015 ];
INF_SP7                   (idx, [1:   8]) = [  1.28411E-03 0.00141 -4.71201E-04 0.00063 -1.12015E-05 0.00407  1.06981E-02 0.00041 ];

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

