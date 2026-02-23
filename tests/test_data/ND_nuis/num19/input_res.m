
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
START_DATE                (idx, [1: 24])  = 'Thu Jan 22 20:17:01 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Fri Jan 23 15:34:12 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.22189E+00  1.01345E+00  9.96043E-01  9.86062E-01  9.80811E-01  9.97787E-01  9.87360E-01  9.94932E-01  9.91294E-01  9.91603E-01  9.95398E-01  9.96195E-01  9.78833E-01  9.91857E-01  9.91222E-01  9.92910E-01  9.98639E-01  9.89139E-01  9.82762E-01  1.00029E+00  9.94527E-01  9.92392E-01  9.87495E-01  9.93149E-01  9.94785E-01  9.94030E-01  9.91957E-01  9.93727E-01  9.94482E-01  9.84979E-01  ];
SHARE_BUF_ARRAY           (idx, 1)        = 0 ;
SHARE_RES2_ARRAY          (idx, 1)        = 1 ;

% File paths:

XS_DATA_FILE_PATH         (idx, [1: 71])  = '/home/thomasligonnet/Documents/XS/xs_lib/jeff33_modif_eurofusion/xsdata' ;
DECAY_DATA_FILE_PATH      (idx, [1:  3])  = 'N/A' ;
SFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
NFY_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;
BRA_DATA_FILE_PATH        (idx, [1:  3])  = 'N/A' ;

% Collision and reaction sampling (neutrons/photons):

MIN_MACROXS               (idx, [1:   4]) = [  2.95583E-01 7.5E-10  0.00000E+00 0.0E+00 ];
DT_THRESH                 (idx, [1:  2])  = [  0.00000E+00  9.00000E-01 ];
ST_FRAC                   (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_FRAC                   (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
DT_EFF                    (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
IFC_COL_EFF               (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_EFF          (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
REA_SAMPLING_FAIL         (idx, [1:   4]) = [  0.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
TMS_SAMPLING_EFF          (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_COL_EFF               (idx, [1:   4]) = [  9.80475E-01 9.4E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.46867E+01 0.00024  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.46776E+01 0.00024  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.68625E+00 0.00024  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.25617E+02 0.00026  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2072554771 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.45426E+05 0.00058 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00006E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.33870E+04 ;
RUNNING_TIME              (idx, 1)        =  1.15718E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.73750E-01  3.73750E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.48333E-03  9.48333E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.15680E+03  1.15680E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.15718E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85192 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88606E+01 3.1E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85686E-01 ;
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

NORM_COEF                 (idx, [1:   4]) = [  3.32927E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.12327E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.41022E-01 1.6E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  5.89779E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32937E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.98946E-01 3.1E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.10297E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.72209E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82507E-01 9.3E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98782E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.29067E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.74935E-02 0.00052 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.01704E+01 5.0E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.43469E+00 1.2E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02226E+02 1.3E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00024E+00 5.4E-05  9.92741E-01 5.1E-05  7.49648E-03 0.00074 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00022E+00 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00017E+00 4.6E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00022E+00 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01805E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.07574E-03 0.00207  6.00425E-05 0.00974  2.99101E-04 0.00446  1.73709E-04 0.00587  3.88854E-04 0.00400  6.68455E-04 0.00317  2.26713E-04 0.00539  1.85089E-04 0.00593  7.37738E-05 0.00950 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.58753E-01 0.00077  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.55838E-03 0.00071  2.26445E-04 0.00402  1.09276E-03 0.00184  6.47909E-04 0.00240  1.42458E-03 0.00161  2.44607E-03 0.00121  8.02623E-04 0.00213  6.67378E-04 0.00235  2.50608E-04 0.00387 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.60766E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.77888E-05 0.00011  4.77687E-05 0.00011  5.04210E-05 0.00099 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.77993E-05 9.5E-05  4.77792E-05 9.5E-05  5.04322E-05 0.00099 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.49494E-03 0.00075  2.24542E-04 0.00440  1.08348E-03 0.00199  6.41023E-04 0.00259  1.41236E-03 0.00174  2.42777E-03 0.00132  7.95454E-04 0.00231  6.61587E-04 0.00255  2.48725E-04 0.00426 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.60827E-01 0.00119  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.70297E-05 0.00022  4.70104E-05 0.00022  4.95279E-05 0.00219 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.70399E-05 0.00021  4.70205E-05 0.00021  4.95392E-05 0.00219 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.62742E-03 0.00217  2.29243E-04 0.01254  1.11169E-03 0.00566  6.60984E-04 0.00728  1.43581E-03 0.00503  2.47624E-03 0.00375  7.95971E-04 0.00673  6.73254E-04 0.00736  2.44228E-04 0.01190 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.55929E-01 0.00334  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.62639E-03 0.00213  2.28832E-04 0.01235  1.11099E-03 0.00555  6.60626E-04 0.00713  1.43575E-03 0.00492  2.47625E-03 0.00368  7.94906E-04 0.00662  6.73933E-04 0.00722  2.45096E-04 0.01171 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.56377E-01 0.00330  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.62295E+02 0.00218 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.74095E-05 6.9E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.74198E-05 4.2E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.60534E-03 0.00042 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.60423E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.38008E-06 5.3E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96061E-06 4.8E-05  1.96045E-06 4.8E-05  1.98147E-06 0.00054 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.15460E-05 7.5E-05  7.16027E-05 7.6E-05  6.40930E-05 0.00087 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.04601E-01 2.1E-05 -3.32503E-02 0.00186  2.43183E-04 0.00187 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.22232E+01 0.00111 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01805E+00 5.5E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.68411E+01 4.4E-05  1.60657E+01 6.4E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.99795E-01 3.0E-05  2.57614E+00 2.8E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  5.00927E-03 8.5E-05  2.72480E-02 3.2E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.75704E-03 7.0E-05  4.98669E-02 5.8E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.74777E-03 6.8E-05  2.26188E-02 9.4E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.55705E-03 6.9E-05  5.45657E-02 9.4E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.60735E+00 7.3E-06  2.41240E+00 2.0E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04434E+02 7.1E-07  2.01942E+02 8.0E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.42434E-08 5.6E-05  3.57850E-06 1.2E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.93030E-01 3.0E-05  2.52627E+00 2.9E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.54386E-01 3.4E-05  5.21443E-01 3.3E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.38330E-01 3.9E-05  8.99534E-02 9.5E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.05085E-03 0.00032  2.38175E-02 0.00028 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.63168E-02 0.00015 -2.04488E-02 0.00028 ];
INF_SCATT5                (idx, [1:   4]) = [ -5.01836E-06 0.42598  1.13992E-02 0.00047 ];
INF_SCATT6                (idx, [1:   4]) = [  7.31390E-03 0.00028 -3.10261E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.02705E-04 0.00228  1.06690E-02 0.00043 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.93086E-01 3.0E-05  2.52627E+00 2.9E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.54389E-01 3.4E-05  5.21443E-01 3.3E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.38331E-01 3.9E-05  8.99534E-02 9.5E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.05104E-03 0.00032  2.38175E-02 0.00028 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.63167E-02 0.00015 -2.04488E-02 0.00028 ];
INF_SCATTP5               (idx, [1:   4]) = [ -5.01212E-06 0.42631  1.13992E-02 0.00047 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.31395E-03 0.00028 -3.10261E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.02742E-04 0.00228  1.06690E-02 0.00043 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.46958E-01 4.0E-05  1.72562E+00 3.5E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.34976E+00 4.0E-05  1.93167E-01 3.5E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.70096E-03 7.0E-05  4.98662E-02 5.8E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.68386E-02 4.2E-05  5.00972E-02 7.1E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 1.5E-09  1.19463E-09 0.84136 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 1.3E-07  1.59549E-07 0.84100 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.62957E-01 3.0E-05  3.00736E-02 4.2E-05  2.28580E-04 0.00066  2.52604E+00 2.9E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.45555E-01 3.4E-05  8.83063E-03 7.7E-05  1.32296E-04 0.00090  5.21310E-01 3.3E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.41407E-01 3.8E-05 -3.07728E-03 0.00016  8.37549E-05 0.00108  8.98696E-02 9.6E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24856E-02 0.00022 -3.43477E-03 0.00014  4.30137E-05 0.00161  2.37745E-02 0.00028 ];
INF_S4                    (idx, [1:   8]) = [ -1.55113E-02 0.00016 -8.05464E-04 0.00047  1.37937E-05 0.00408 -2.04626E-02 0.00028 ];
INF_S5                    (idx, [1:   8]) = [ -3.42622E-04 0.00621  3.37604E-04 0.00116 -2.62192E-06 0.01993  1.14018E-02 0.00047 ];
INF_S6                    (idx, [1:   8]) = [  7.58239E-03 0.00027 -2.68496E-04 0.00122 -9.56682E-06 0.00486 -3.10165E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.27621E-03 0.00142 -4.73508E-04 0.00064 -1.14384E-05 0.00387  1.06804E-02 0.00043 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.63013E-01 3.0E-05  3.00736E-02 4.2E-05  2.28581E-04 0.00066  2.52604E+00 2.9E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.45558E-01 3.4E-05  8.83063E-03 7.7E-05  1.32296E-04 0.00090  5.21310E-01 3.3E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.41408E-01 3.8E-05 -3.07728E-03 0.00016  8.37549E-05 0.00108  8.98697E-02 9.6E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24858E-02 0.00022 -3.43477E-03 0.00014  4.30137E-05 0.00161  2.37745E-02 0.00028 ];
INF_SP4                   (idx, [1:   8]) = [ -1.55113E-02 0.00016 -8.05464E-04 0.00047  1.37937E-05 0.00408 -2.04626E-02 0.00028 ];
INF_SP5                   (idx, [1:   8]) = [ -3.42616E-04 0.00621  3.37604E-04 0.00116 -2.62193E-06 0.01993  1.14018E-02 0.00047 ];
INF_SP6                   (idx, [1:   8]) = [  7.58244E-03 0.00027 -2.68496E-04 0.00122 -9.56683E-06 0.00486 -3.10165E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.27625E-03 0.00142 -4.73508E-04 0.00064 -1.14384E-05 0.00387  1.06804E-02 0.00043 ];

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

