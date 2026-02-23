
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
START_DATE                (idx, [1: 24])  = 'Mon Jan 19 14:17:42 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Tue Jan 20 10:00:31 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.22033E+00  9.93761E-01  9.87865E-01  9.93490E-01  9.90900E-01  1.00419E+00  9.93874E-01  9.83672E-01  9.88271E-01  9.84055E-01  9.88117E-01  9.98057E-01  9.91605E-01  9.96198E-01  9.90452E-01  9.88002E-01  9.98640E-01  9.83457E-01  9.93251E-01  9.94323E-01  9.92245E-01  9.99416E-01  9.89706E-01  1.00218E+00  9.80462E-01  9.97182E-01  9.92271E-01  9.97215E-01  9.99795E-01  9.87025E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.81099E-01 9.1E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.61769E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.61675E+01 0.00022  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.66004E+00 0.00022  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26808E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2079089412 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.46515E+05 0.00051 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.41406E+04 ;
RUNNING_TIME              (idx, 1)        =  1.18281E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.71283E-01  3.71283E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.00000E-03  9.00000E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.18243E+03  1.18243E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.18281E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.86404 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88719E+01 3.2E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85863E-01 ;
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

NORM_COEF                 (idx, [1:   4]) = [  3.32915E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.16617E-01 9.9E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.41041E-01 1.6E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  5.89587E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.33123E-11 3.1E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.00557E+00 3.1E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.10872E-01 3.1E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.71832E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82704E-01 9.5E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98745E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.33703E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.72959E-02 0.00054 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.12273E+01 5.1E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44741E+00 1.2E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02226E+02 1.3E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00688E+00 5.3E-05  9.99346E-01 5.0E-05  7.51155E-03 0.00073 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00687E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00684E+00 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00687E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.02461E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  1.99519E-03 0.00210  5.70603E-05 0.00853  2.89276E-04 0.00449  1.65106E-04 0.00558  3.71268E-04 0.00382  6.46595E-04 0.00325  2.16201E-04 0.00506  1.78925E-04 0.00587  7.07544E-05 0.00947 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.58888E-01 0.00076  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.52733E-03 0.00069  2.25647E-04 0.00399  1.08743E-03 0.00179  6.43341E-04 0.00236  1.42246E-03 0.00157  2.43427E-03 0.00120  8.00915E-04 0.00214  6.64724E-04 0.00229  2.48548E-04 0.00385 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.60471E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.79561E-05 0.00011  4.79347E-05 0.00011  5.07662E-05 0.00101 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.82852E-05 9.2E-05  4.82638E-05 9.3E-05  5.11145E-05 0.00101 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.45992E-03 0.00075  2.23914E-04 0.00433  1.07638E-03 0.00195  6.38998E-04 0.00256  1.40685E-03 0.00170  2.41611E-03 0.00133  7.93639E-04 0.00230  6.58074E-04 0.00248  2.45953E-04 0.00414 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.60252E-01 0.00118  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.71774E-05 0.00021  4.71569E-05 0.00021  4.98723E-05 0.00218 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.75013E-05 0.00021  4.74806E-05 0.00021  5.02149E-05 0.00218 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.57656E-03 0.00211  2.29943E-04 0.01247  1.09654E-03 0.00557  6.54744E-04 0.00731  1.43645E-03 0.00490  2.45605E-03 0.00373  7.99357E-04 0.00662  6.60114E-04 0.00722  2.43370E-04 0.01188 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.54593E-01 0.00330  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.58049E-03 0.00207  2.30223E-04 0.01216  1.09681E-03 0.00547  6.53651E-04 0.00714  1.43666E-03 0.00479  2.45669E-03 0.00365  8.00617E-04 0.00645  6.62584E-04 0.00708  2.43246E-04 0.01157 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.54970E-01 0.00321  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.60716E+02 0.00212 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.75690E-05 6.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.78955E-05 4.1E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.55912E-03 0.00041 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.58913E+02 0.00042 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38756E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96212E-06 4.8E-05  1.96198E-06 4.8E-05  1.98062E-06 0.00053 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.29161E-05 7.6E-05  7.29762E-05 7.6E-05  6.49703E-05 0.00086 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02792E-01 2.1E-05 -3.45172E-02 0.00184  2.50636E-04 0.00184 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.22194E+01 0.00111 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.02455E+00 5.6E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.70672E+01 4.3E-05  1.63032E+01 6.8E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  7.02563E-01 2.8E-05  2.58914E+00 3.1E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.01933E-03 8.1E-05  2.67418E-02 3.2E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.77578E-03 6.6E-05  4.90277E-02 6.1E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.75645E-03 5.6E-05  2.22860E-02 0.00010 ];
INF_NSF                   (idx, [1:   4]) = [  4.60809E-03 5.7E-05  5.40294E-02 0.00010 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.62353E+00 7.4E-06  2.42437E+00 2.3E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04404E+02 7.3E-07  2.01942E+02 7.5E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.36455E-08 5.1E-05  3.58562E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.95777E-01 2.8E-05  2.54011E+00 3.3E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.51377E-01 3.1E-05  5.21993E-01 3.3E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37299E-01 3.8E-05  8.98087E-02 9.2E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.07448E-03 0.00030  2.37681E-02 0.00028 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.60598E-02 0.00015 -2.05078E-02 0.00028 ];
INF_SCATT5                (idx, [1:   4]) = [  4.47836E-05 0.04882  1.14537E-02 0.00045 ];
INF_SCATT6                (idx, [1:   4]) = [  7.26038E-03 0.00027 -3.11055E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.11538E-04 0.00218  1.07301E-02 0.00042 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.95834E-01 2.8E-05  2.54011E+00 3.3E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.51380E-01 3.1E-05  5.21993E-01 3.3E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37300E-01 3.8E-05  8.98087E-02 9.2E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.07465E-03 0.00030  2.37681E-02 0.00028 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.60597E-02 0.00015 -2.05078E-02 0.00028 ];
INF_SCATTP5               (idx, [1:   4]) = [  4.48139E-05 0.04879  1.14537E-02 0.00045 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.26043E-03 0.00027 -3.11055E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.11553E-04 0.00218  1.07301E-02 0.00042 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.49499E-01 3.9E-05  1.74042E+00 4.0E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.33601E+00 3.9E-05  1.91524E-01 4.0E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.71948E-03 6.7E-05  4.90271E-02 6.1E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.65423E-02 4.1E-05  4.92580E-02 7.5E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 3.0E-09  3.44928E-09 0.87087 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 4.2E-07  4.80705E-07 0.87414 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.66021E-01 2.8E-05  2.97563E-02 3.9E-05  2.28355E-04 0.00069  2.53988E+00 3.3E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.42662E-01 3.1E-05  8.71559E-03 7.0E-05  1.30619E-04 0.00093  5.21863E-01 3.3E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40343E-01 3.7E-05 -3.04380E-03 0.00018  8.22194E-05 0.00108  8.97265E-02 9.2E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24700E-02 0.00021 -3.39551E-03 0.00013  4.21414E-05 0.00159  2.37260E-02 0.00028 ];
INF_S4                    (idx, [1:   8]) = [ -1.52643E-02 0.00015 -7.95501E-04 0.00047  1.34662E-05 0.00441 -2.05213E-02 0.00028 ];
INF_S5                    (idx, [1:   8]) = [ -2.89647E-04 0.00743  3.34431E-04 0.00111 -2.56889E-06 0.01975  1.14563E-02 0.00045 ];
INF_S6                    (idx, [1:   8]) = [  7.52548E-03 0.00026 -2.65100E-04 0.00126 -9.37607E-06 0.00501 -3.10962E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.27943E-03 0.00136 -4.67895E-04 0.00068 -1.11496E-05 0.00404  1.07412E-02 0.00042 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.66077E-01 2.8E-05  2.97563E-02 3.9E-05  2.28355E-04 0.00069  2.53988E+00 3.3E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.42664E-01 3.1E-05  8.71559E-03 7.0E-05  1.30619E-04 0.00093  5.21863E-01 3.3E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40344E-01 3.7E-05 -3.04380E-03 0.00018  8.22194E-05 0.00108  8.97265E-02 9.2E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24702E-02 0.00021 -3.39552E-03 0.00013  4.21414E-05 0.00159  2.37260E-02 0.00028 ];
INF_SP4                   (idx, [1:   8]) = [ -1.52642E-02 0.00015 -7.95501E-04 0.00047  1.34662E-05 0.00441 -2.05213E-02 0.00028 ];
INF_SP5                   (idx, [1:   8]) = [ -2.89617E-04 0.00743  3.34431E-04 0.00111 -2.56889E-06 0.01975  1.14563E-02 0.00045 ];
INF_SP6                   (idx, [1:   8]) = [  7.52553E-03 0.00026 -2.65101E-04 0.00126 -9.37606E-06 0.00501 -3.10962E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.27945E-03 0.00137 -4.67895E-04 0.00068 -1.11495E-05 0.00404  1.07412E-02 0.00042 ];

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

