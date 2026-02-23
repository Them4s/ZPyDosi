
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
START_DATE                (idx, [1: 24])  = 'Sun Jan 25 07:19:02 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Mon Jan 26 03:05:00 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.19632E+00  1.00577E+00  9.96860E-01  9.95155E-01  1.00508E+00  9.97424E-01  9.96760E-01  9.87366E-01  1.00344E+00  9.80258E-01  1.00544E+00  1.00096E+00  9.94952E-01  9.86788E-01  9.90041E-01  9.94339E-01  9.82058E-01  9.90009E-01  9.96605E-01  9.84848E-01  9.85055E-01  9.88848E-01  9.87290E-01  9.92837E-01  9.99549E-01  9.97033E-01  9.84308E-01  9.84307E-01  9.97870E-01  9.92416E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.80891E-01 9.6E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.59200E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.59106E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.67363E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26527E+02 0.00025  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2104478128 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.50746E+05 0.00055 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.42236E+04 ;
RUNNING_TIME              (idx, 1)        =  1.18598E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.71533E-01  3.71533E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.21667E-03  9.21667E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.18560E+03  1.18560E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.18598E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85682 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88646E+01 3.0E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85795E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.25 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32913E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.12546E-01 1.0E-04 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.40100E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  5.98997E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32901E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.99094E-01 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.10176E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.72306E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82482E-01 9.5E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98738E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.33306E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.75180E-02 0.00053 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.10889E+01 5.1E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.43577E+00 1.2E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02231E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00030E+00 5.2E-05  9.92773E-01 5.0E-05  7.50961E-03 0.00073 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00038E+00 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00036E+00 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00038E+00 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01824E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.00944E-03 0.00201  5.72215E-05 0.00918  2.90115E-04 0.00428  1.65894E-04 0.00528  3.75492E-04 0.00393  6.48481E-04 0.00295  2.21804E-04 0.00526  1.79827E-04 0.00532  7.06048E-05 0.00869 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.60059E-01 0.00075  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.57657E-03 0.00068  2.25555E-04 0.00402  1.09629E-03 0.00180  6.45522E-04 0.00236  1.42612E-03 0.00157  2.45114E-03 0.00121  8.08896E-04 0.00216  6.71470E-04 0.00229  2.51571E-04 0.00376 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.61820E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.81512E-05 0.00011  4.81312E-05 0.00011  5.07846E-05 0.00098 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.81650E-05 9.3E-05  4.81449E-05 9.4E-05  5.07987E-05 0.00098 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.50678E-03 0.00075  2.24007E-04 0.00430  1.08724E-03 0.00195  6.38883E-04 0.00255  1.41381E-03 0.00170  2.42601E-03 0.00133  8.03898E-04 0.00230  6.64084E-04 0.00249  2.48844E-04 0.00411 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.61522E-01 0.00117  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.73829E-05 0.00022  4.73635E-05 0.00022  4.99317E-05 0.00221 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.73964E-05 0.00021  4.73770E-05 0.00021  4.99470E-05 0.00221 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.59201E-03 0.00214  2.27834E-04 0.01213  1.09193E-03 0.00558  6.54621E-04 0.00730  1.44598E-03 0.00491  2.45784E-03 0.00380  7.99554E-04 0.00660  6.69359E-04 0.00720  2.44894E-04 0.01173 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.57162E-01 0.00325  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.59702E-03 0.00211  2.28974E-04 0.01185  1.09281E-03 0.00547  6.54036E-04 0.00716  1.44724E-03 0.00481  2.46015E-03 0.00372  7.99859E-04 0.00649  6.68319E-04 0.00705  2.45633E-04 0.01150 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.57059E-01 0.00318  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.60345E+02 0.00216 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.77653E-05 6.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.77789E-05 4.1E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.59607E-03 0.00043 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.59034E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38775E-06 5.2E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.95940E-06 4.8E-05  1.95925E-06 4.8E-05  1.97884E-06 0.00055 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.28332E-05 7.6E-05  7.28937E-05 7.6E-05  6.48939E-05 0.00084 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.03098E-01 2.1E-05 -3.43078E-02 0.00183  2.50763E-04 0.00184 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21815E+01 0.00110 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01825E+00 5.4E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.70384E+01 4.3E-05  1.62924E+01 6.6E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.99152E-01 2.9E-05  2.58926E+00 3.3E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.99286E-03 7.9E-05  2.68414E-02 3.3E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.76342E-03 6.5E-05  4.90791E-02 5.9E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.77056E-03 6.4E-05  2.22377E-02 9.7E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.61581E-03 6.5E-05  5.36629E-02 9.7E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.60699E+00 7.3E-06  2.41315E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04422E+02 7.2E-07  2.01942E+02 7.5E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.36392E-08 5.4E-05  3.58525E-06 1.3E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.92380E-01 2.9E-05  2.54018E+00 3.4E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.52001E-01 3.3E-05  5.22251E-01 3.8E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37540E-01 3.8E-05  8.98703E-02 8.6E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.09999E-03 0.00030  2.37932E-02 0.00028 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61014E-02 0.00014 -2.05296E-02 0.00029 ];
INF_SCATT5                (idx, [1:   4]) = [  4.69800E-05 0.04544  1.14465E-02 0.00046 ];
INF_SCATT6                (idx, [1:   4]) = [  7.28585E-03 0.00029 -3.11127E-02 0.00015 ];
INF_SCATT7                (idx, [1:   4]) = [  8.14091E-04 0.00228  1.07301E-02 0.00043 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.92436E-01 2.9E-05  2.54018E+00 3.4E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.52003E-01 3.3E-05  5.22251E-01 3.8E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37541E-01 3.8E-05  8.98703E-02 8.6E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.10019E-03 0.00030  2.37933E-02 0.00028 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61014E-02 0.00014 -2.05296E-02 0.00029 ];
INF_SCATTP5               (idx, [1:   4]) = [  4.69915E-05 0.04544  1.14465E-02 0.00046 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.28588E-03 0.00029 -3.11127E-02 0.00015 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.14126E-04 0.00228  1.07301E-02 0.00043 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.44197E-01 3.9E-05  1.73974E+00 3.9E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.36502E+00 3.9E-05  1.91600E-01 3.9E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.70694E-03 6.5E-05  4.90785E-02 5.9E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.65710E-02 4.3E-05  4.93079E-02 7.5E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  2.03414E-10 0.53971 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 1.5E-08  2.75701E-08 0.54009 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.62581E-01 2.9E-05  2.97990E-02 4.1E-05  2.28215E-04 0.00066  2.53995E+00 3.4E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.43269E-01 3.3E-05  8.73196E-03 7.8E-05  1.30616E-04 0.00086  5.22121E-01 3.8E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40587E-01 3.8E-05 -3.04709E-03 0.00018  8.23226E-05 0.00113  8.97880E-02 8.6E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.25009E-02 0.00021 -3.40093E-03 0.00013  4.21373E-05 0.00171  2.37511E-02 0.00028 ];
INF_S4                    (idx, [1:   8]) = [ -1.53038E-02 0.00015 -7.97581E-04 0.00050  1.33855E-05 0.00423 -2.05430E-02 0.00029 ];
INF_S5                    (idx, [1:   8]) = [ -2.87704E-04 0.00740  3.34684E-04 0.00111 -2.71175E-06 0.01876  1.14492E-02 0.00046 ];
INF_S6                    (idx, [1:   8]) = [  7.55147E-03 0.00027 -2.65612E-04 0.00125 -9.56035E-06 0.00530 -3.11031E-02 0.00015 ];
INF_S7                    (idx, [1:   8]) = [  1.28273E-03 0.00142 -4.68638E-04 0.00070 -1.13603E-05 0.00389  1.07415E-02 0.00043 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.62637E-01 2.9E-05  2.97990E-02 4.1E-05  2.28216E-04 0.00065  2.53995E+00 3.4E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.43271E-01 3.3E-05  8.73196E-03 7.8E-05  1.30617E-04 0.00086  5.22121E-01 3.8E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40588E-01 3.8E-05 -3.04709E-03 0.00018  8.23225E-05 0.00113  8.97880E-02 8.6E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.25011E-02 0.00021 -3.40093E-03 0.00013  4.21373E-05 0.00171  2.37511E-02 0.00028 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53038E-02 0.00015 -7.97581E-04 0.00050  1.33855E-05 0.00423 -2.05430E-02 0.00029 ];
INF_SP5                   (idx, [1:   8]) = [ -2.87693E-04 0.00740  3.34684E-04 0.00111 -2.71175E-06 0.01876  1.14492E-02 0.00046 ];
INF_SP6                   (idx, [1:   8]) = [  7.55149E-03 0.00027 -2.65612E-04 0.00125 -9.56035E-06 0.00530 -3.11031E-02 0.00015 ];
INF_SP7                   (idx, [1:   8]) = [  1.28276E-03 0.00142 -4.68638E-04 0.00070 -1.13603E-05 0.00389  1.07415E-02 0.00043 ];

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

