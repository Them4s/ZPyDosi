
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
START_DATE                (idx, [1: 24])  = 'Tue Jan 20 09:10:31 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Wed Jan 21 04:44:33 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.20612E+00  1.00524E+00  9.92027E-01  1.01474E+00  9.89327E-01  1.00029E+00  9.95226E-01  9.88446E-01  9.91987E-01  9.93502E-01  9.97062E-01  9.92921E-01  9.92126E-01  9.96932E-01  9.41844E-01  9.95960E-01  1.00411E+00  1.00487E+00  9.90090E-01  9.87383E-01  9.84900E-01  9.85627E-01  9.95159E-01  9.95937E-01  9.88018E-01  9.98826E-01  9.88180E-01  1.00082E+00  9.85264E-01  9.97064E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.80781E-01 9.5E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.59891E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.59796E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.68480E+00 0.00021  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.26243E+02 0.00023  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2091606211 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.48601E+05 0.00049 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.38816E+04 ;
RUNNING_TIME              (idx, 1)        =  1.17404E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.74233E-01  3.74233E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.11667E-03  9.11667E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.17365E+03  1.17365E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.17403E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85904 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88669E+01 3.1E-05 ];
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

NORM_COEF                 (idx, [1:   4]) = [  3.32894E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.15298E-01 0.00010 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.40220E-01 1.7E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  5.97796E-02 0.00026 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.33087E-11 3.2E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  1.00408E+00 3.2E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.10751E-01 3.2E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.71645E-01 2.4E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82397E-01 9.4E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98682E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.34048E+01 3.1E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.76030E-02 0.00052 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.12692E+01 5.1E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44450E+00 1.4E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02230E+02 1.3E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  1.00551E+00 5.3E-05  9.97991E-01 5.1E-05  7.50535E-03 0.00073 ];
IMP_KEFF                  (idx, [1:   2]) = [  1.00538E+00 3.2E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  1.00541E+00 4.6E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  1.00538E+00 3.2E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.02341E+00 3.0E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  2.02638E-03 0.00208  5.78843E-05 0.00913  2.94473E-04 0.00471  1.65735E-04 0.00517  3.79611E-04 0.00411  6.53161E-04 0.00307  2.21111E-04 0.00511  1.82639E-04 0.00554  7.17692E-05 0.01024 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.59649E-01 0.00075  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.53995E-03 0.00069  2.23718E-04 0.00410  1.09246E-03 0.00183  6.42005E-04 0.00236  1.42324E-03 0.00163  2.43730E-03 0.00119  8.02856E-04 0.00215  6.67748E-04 0.00232  2.50630E-04 0.00381 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.61612E-01 0.00108  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.83491E-05 0.00011  4.83275E-05 0.00011  5.11876E-05 0.00099 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.86146E-05 9.3E-05  4.85929E-05 9.4E-05  5.14688E-05 0.00099 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.46256E-03 0.00075  2.23392E-04 0.00443  1.08053E-03 0.00198  6.36643E-04 0.00260  1.40815E-03 0.00174  2.41099E-03 0.00132  7.93149E-04 0.00230  6.61564E-04 0.00251  2.48134E-04 0.00421 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.61694E-01 0.00119  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.75667E-05 0.00022  4.75449E-05 0.00022  5.04038E-05 0.00221 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.78279E-05 0.00021  4.78060E-05 0.00021  5.06801E-05 0.00221 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.59287E-03 0.00215  2.26430E-04 0.01235  1.09497E-03 0.00567  6.49311E-04 0.00746  1.43867E-03 0.00499  2.46623E-03 0.00380  7.98143E-04 0.00658  6.70615E-04 0.00729  2.48496E-04 0.01202 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.58968E-01 0.00342  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.59011E-03 0.00210  2.27221E-04 0.01218  1.09447E-03 0.00554  6.50315E-04 0.00731  1.43645E-03 0.00487  2.46503E-03 0.00370  7.98823E-04 0.00644  6.68951E-04 0.00712  2.48845E-04 0.01175 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.59052E-01 0.00335  1.24667E-02 5.1E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.59747E+02 0.00216 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.79703E-05 6.7E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.82337E-05 4.0E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.56942E-03 0.00043 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.57798E+02 0.00044 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.40147E-06 5.4E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96216E-06 4.7E-05  1.96200E-06 4.7E-05  1.98274E-06 0.00054 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.35345E-05 7.7E-05  7.35951E-05 7.7E-05  6.55522E-05 0.00087 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.04908E-01 2.1E-05 -3.40622E-02 0.00185  2.48185E-04 0.00185 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21942E+01 0.00112 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.02351E+00 5.1E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.69314E+01 4.1E-05  1.64735E+01 6.8E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.96474E-01 2.9E-05  2.58066E+00 2.7E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.99259E-03 8.0E-05  2.65391E-02 3.5E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.72310E-03 6.5E-05  4.86442E-02 6.1E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.73051E-03 6.2E-05  2.21052E-02 9.6E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.58193E-03 6.3E-05  5.34611E-02 9.6E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.64774E+00 8.5E-06  2.41849E+00 1.5E-09 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04486E+02 7.0E-07  2.01942E+02 7.4E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.40890E-08 5.3E-05  3.58789E-06 1.4E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.89744E-01 2.9E-05  2.53202E+00 2.8E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.53238E-01 3.3E-05  5.21869E-01 3.2E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.37854E-01 3.9E-05  8.97789E-02 9.1E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.02767E-03 0.00030  2.37812E-02 0.00028 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.62489E-02 0.00014 -2.05311E-02 0.00028 ];
INF_SCATT5                (idx, [1:   4]) = [  2.25247E-05 0.08639  1.14559E-02 0.00047 ];
INF_SCATT6                (idx, [1:   4]) = [  7.31316E-03 0.00027 -3.11540E-02 0.00016 ];
INF_SCATT7                (idx, [1:   4]) = [  8.15827E-04 0.00236  1.07581E-02 0.00045 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.89801E-01 2.9E-05  2.53202E+00 2.8E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.53241E-01 3.3E-05  5.21869E-01 3.2E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.37855E-01 3.9E-05  8.97789E-02 9.1E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.02786E-03 0.00030  2.37812E-02 0.00028 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.62489E-02 0.00014 -2.05311E-02 0.00028 ];
INF_SCATTP5               (idx, [1:   4]) = [  2.25345E-05 0.08639  1.14559E-02 0.00047 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.31320E-03 0.00027 -3.11540E-02 0.00016 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.15833E-04 0.00236  1.07581E-02 0.00045 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.44669E-01 3.6E-05  1.73045E+00 3.3E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.36239E+00 3.6E-05  1.92628E-01 3.3E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.66640E-03 6.6E-05  4.86435E-02 6.1E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.67109E-02 4.1E-05  4.88653E-02 7.4E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  6.62296E-10 0.73779 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  0.00000E+00 0.0E+00 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 6.3E-08  8.58470E-08 0.73186 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.59763E-01 2.8E-05  2.99810E-02 3.9E-05  2.22632E-04 0.00064  2.53179E+00 2.8E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.44429E-01 3.3E-05  8.80848E-03 7.9E-05  1.28903E-04 0.00084  5.21740E-01 3.2E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.40921E-01 3.8E-05 -3.06765E-03 0.00018  8.16985E-05 0.00102  8.96972E-02 9.1E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24532E-02 0.00021 -3.42549E-03 0.00014  4.20297E-05 0.00165  2.37392E-02 0.00028 ];
INF_S4                    (idx, [1:   8]) = [ -1.54457E-02 0.00015 -8.03209E-04 0.00047  1.34621E-05 0.00432 -2.05446E-02 0.00028 ];
INF_S5                    (idx, [1:   8]) = [ -3.14343E-04 0.00607  3.36868E-04 0.00108 -2.59272E-06 0.02045  1.14585E-02 0.00047 ];
INF_S6                    (idx, [1:   8]) = [  7.58115E-03 0.00025 -2.67995E-04 0.00123 -9.32024E-06 0.00523 -3.11447E-02 0.00016 ];
INF_S7                    (idx, [1:   8]) = [  1.28793E-03 0.00148 -4.72100E-04 0.00067 -1.11222E-05 0.00399  1.07692E-02 0.00045 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.59820E-01 2.8E-05  2.99810E-02 3.9E-05  2.22633E-04 0.00064  2.53179E+00 2.8E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.44432E-01 3.3E-05  8.80848E-03 7.9E-05  1.28903E-04 0.00084  5.21740E-01 3.2E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.40923E-01 3.8E-05 -3.06765E-03 0.00018  8.16985E-05 0.00102  8.96972E-02 9.1E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24534E-02 0.00021 -3.42550E-03 0.00014  4.20297E-05 0.00165  2.37392E-02 0.00028 ];
INF_SP4                   (idx, [1:   8]) = [ -1.54457E-02 0.00015 -8.03209E-04 0.00047  1.34621E-05 0.00432 -2.05446E-02 0.00028 ];
INF_SP5                   (idx, [1:   8]) = [ -3.14333E-04 0.00607  3.36868E-04 0.00108 -2.59273E-06 0.02045  1.14585E-02 0.00047 ];
INF_SP6                   (idx, [1:   8]) = [  7.58120E-03 0.00025 -2.67995E-04 0.00123 -9.32024E-06 0.00523 -3.11447E-02 0.00016 ];
INF_SP7                   (idx, [1:   8]) = [  1.28793E-03 0.00148 -4.72100E-04 0.00067 -1.11221E-05 0.00399  1.07692E-02 0.00045 ];

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

