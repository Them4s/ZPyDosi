
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
START_DATE                (idx, [1: 24])  = 'Wed Jan 21 04:44:35 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Thu Jan 22 00:19:56 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.20845E+00  1.00607E+00  9.95214E-01  9.91277E-01  9.83206E-01  9.98555E-01  9.96042E-01  9.81662E-01  9.57999E-01  1.00204E+00  9.91887E-01  9.95617E-01  9.90514E-01  9.95645E-01  9.97376E-01  1.00183E+00  9.97263E-01  9.88195E-01  9.92373E-01  9.94653E-01  1.00360E+00  9.98267E-01  9.85670E-01  9.87996E-01  9.86784E-01  9.90342E-01  9.91021E-01  1.00346E+00  9.96099E-01  9.90904E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.81323E-01 9.6E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.65075E+01 0.00020  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.64984E+01 0.00020  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.64630E+00 0.00021  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26459E+02 0.00023  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2082918537 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.47153E+05 0.00051 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.39173E+04 ;
RUNNING_TIME              (idx, 1)        =  1.17535E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.70717E-01  3.70717E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.13333E-03  9.13333E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.17497E+03  1.17497E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.17535E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85720 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88651E+01 3.2E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85745E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.23 ;

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

CONVERSION_RATIO          (idx, [1:   2]) = [  5.08811E-01 9.9E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.39680E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.03203E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.33558E-11 3.1E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.01734E+00 3.1E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.12199E-01 3.1E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.70603E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82802E-01 9.4E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98738E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.33739E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.71978E-02 0.00054 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.15763E+01 5.1E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.46808E+00 1.3E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02233E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.01864E+00 5.3E-05  1.01111E+00 5.0E-05  7.53109E-03 0.00072 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.01864E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.01863E+00 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.01864E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.03649E+00 2.9E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  1.96660E-03 0.00190  5.52608E-05 0.00895  2.84696E-04 0.00423  1.63178E-04 0.00525  3.67080E-04 0.00389  6.35261E-04 0.00292  2.15768E-04 0.00522  1.76310E-04 0.00544  6.90418E-05 0.00893 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.59715E-01 0.00076  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.46465E-03 0.00069  2.18682E-04 0.00397  1.08099E-03 0.00183  6.34810E-04 0.00231  1.40730E-03 0.00161  2.42061E-03 0.00120  7.94444E-04 0.00214  6.58706E-04 0.00232  2.49114E-04 0.00382 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.61815E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.76073E-05 0.00011  4.75868E-05 0.00011  5.03322E-05 0.00099 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.84940E-05 9.3E-05  4.84731E-05 9.3E-05  5.12696E-05 0.00099 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.39435E-03 0.00074  2.18400E-04 0.00434  1.06977E-03 0.00196  6.28941E-04 0.00256  1.39120E-03 0.00174  2.39727E-03 0.00131  7.87031E-04 0.00232  6.53978E-04 0.00253  2.47762E-04 0.00415 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.62541E-01 0.00118  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.68350E-05 0.00022  4.68151E-05 0.00022  4.94314E-05 0.00223 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.77072E-05 0.00021  4.76870E-05 0.00021  5.03519E-05 0.00223 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.51965E-03 0.00217  2.25183E-04 0.01223  1.08506E-03 0.00573  6.40890E-04 0.00746  1.42472E-03 0.00492  2.43808E-03 0.00385  7.92104E-04 0.00668  6.64986E-04 0.00716  2.48637E-04 0.01206 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.60281E-01 0.00333  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.51785E-03 0.00213  2.26873E-04 0.01208  1.08596E-03 0.00562  6.39455E-04 0.00732  1.42522E-03 0.00484  2.43562E-03 0.00377  7.91600E-04 0.00653  6.64113E-04 0.00702  2.49007E-04 0.01188 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.60266E-01 0.00329  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.60662E+02 0.00218 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.72226E-05 6.8E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.81022E-05 4.3E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.49767E-03 0.00043 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.58777E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.39929E-06 5.2E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96092E-06 4.8E-05  1.96077E-06 4.9E-05  1.98048E-06 0.00054 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.34237E-05 7.5E-05  7.34832E-05 7.5E-05  6.55116E-05 0.00087 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.04254E-01 2.1E-05 -3.48796E-02 0.00174  2.51606E-04 0.00175 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21924E+01 0.00110 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.03650E+00 5.1E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.69385E+01 4.2E-05  1.64355E+01 6.5E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  7.04403E-01 3.0E-05  2.59202E+00 2.9E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.98901E-03 8.5E-05  2.65407E-02 3.5E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.75663E-03 6.9E-05  4.87235E-02 5.8E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.76763E-03 5.9E-05  2.21828E-02 9.1E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.69982E-03 6.0E-05  5.41961E-02 9.1E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.65883E+00 8.0E-06  2.44316E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04466E+02 7.0E-07  2.01942E+02 8.0E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.39556E-08 5.5E-05  3.58799E-06 1.3E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.97637E-01 3.0E-05  2.54329E+00 3.0E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.53299E-01 3.3E-05  5.22329E-01 3.4E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.38046E-01 3.9E-05  8.97925E-02 9.3E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.10629E-03 0.00028  2.37684E-02 0.00028 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.61754E-02 0.00016 -2.05357E-02 0.00028 ];
INF_SCATT5                (idx, [1:   4]) = [  3.37851E-05 0.06997  1.14564E-02 0.00046 ];
INF_SCATT6                (idx, [1:   4]) = [  7.30046E-03 0.00028 -3.11479E-02 0.00017 ];
INF_SCATT7                (idx, [1:   4]) = [  8.11113E-04 0.00229  1.07583E-02 0.00042 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.97694E-01 3.0E-05  2.54329E+00 3.0E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.53302E-01 3.3E-05  5.22329E-01 3.4E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.38047E-01 3.9E-05  8.97925E-02 9.3E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.10648E-03 0.00028  2.37684E-02 0.00028 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.61753E-02 0.00016 -2.05357E-02 0.00028 ];
INF_SCATTP5               (idx, [1:   4]) = [  3.38063E-05 0.07004  1.14564E-02 0.00046 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.30049E-03 0.00028 -3.11479E-02 0.00017 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.11120E-04 0.00229  1.07583E-02 0.00042 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.48934E-01 3.9E-05  1.74301E+00 3.6E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.33905E+00 3.9E-05  1.91241E-01 3.6E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.70030E-03 7.0E-05  4.87228E-02 5.8E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.67183E-02 4.6E-05  4.89509E-02 7.0E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  6.10838E-10 0.70625 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 5.7E-08  8.02189E-08 0.70788 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.67685E-01 3.0E-05  2.99529E-02 4.0E-05  2.27133E-04 0.00065  2.54307E+00 3.0E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.44527E-01 3.3E-05  8.77240E-03 7.6E-05  1.29793E-04 0.00086  5.22199E-01 3.4E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.41108E-01 3.8E-05 -3.06200E-03 0.00017  8.16432E-05 0.00107  8.97109E-02 9.3E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.25240E-02 0.00020 -3.41771E-03 0.00013  4.18118E-05 0.00167  2.37266E-02 0.00028 ];
INF_S4                    (idx, [1:   8]) = [ -1.53734E-02 0.00016 -8.02035E-04 0.00050  1.33423E-05 0.00451 -2.05491E-02 0.00028 ];
INF_S5                    (idx, [1:   8]) = [ -3.02247E-04 0.00771  3.36032E-04 0.00111 -2.60343E-06 0.02004  1.14590E-02 0.00046 ];
INF_S6                    (idx, [1:   8]) = [  7.56723E-03 0.00027 -2.66776E-04 0.00120 -9.35249E-06 0.00485 -3.11386E-02 0.00017 ];
INF_S7                    (idx, [1:   8]) = [  1.28188E-03 0.00143 -4.70764E-04 0.00068 -1.11389E-05 0.00397  1.07695E-02 0.00042 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.67741E-01 3.0E-05  2.99529E-02 4.0E-05  2.27133E-04 0.00065  2.54307E+00 3.0E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.44530E-01 3.3E-05  8.77240E-03 7.6E-05  1.29793E-04 0.00086  5.22199E-01 3.4E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.41109E-01 3.8E-05 -3.06200E-03 0.00017  8.16432E-05 0.00107  8.97109E-02 9.3E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.25242E-02 0.00020 -3.41771E-03 0.00013  4.18118E-05 0.00167  2.37266E-02 0.00028 ];
INF_SP4                   (idx, [1:   8]) = [ -1.53733E-02 0.00016 -8.02035E-04 0.00050  1.33423E-05 0.00451 -2.05491E-02 0.00028 ];
INF_SP5                   (idx, [1:   8]) = [ -3.02226E-04 0.00773  3.36032E-04 0.00111 -2.60343E-06 0.02004  1.14590E-02 0.00046 ];
INF_SP6                   (idx, [1:   8]) = [  7.56727E-03 0.00027 -2.66776E-04 0.00120 -9.35250E-06 0.00485 -3.11386E-02 0.00017 ];
INF_SP7                   (idx, [1:   8]) = [  1.28188E-03 0.00143 -4.70764E-04 0.00068 -1.11389E-05 0.00397  1.07695E-02 0.00042 ];

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

