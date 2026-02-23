
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
START_DATE                (idx, [1: 24])  = 'Mon Jan 26 02:23:50 2026' ;
COMPLETE_DATE             (idx, [1: 24])  = 'Mon Jan 26 22:13:39 2026' ;

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
OMP_HISTORY_PROFILE       (idx, [1:  30]) = [  1.20990E+00  1.00828E+00  9.87508E-01  9.98980E-01  9.84033E-01  9.87595E-01  9.85965E-01  9.94325E-01  9.90680E-01  9.92796E-01  9.93703E-01  1.00022E+00  9.89323E-01  9.90279E-01  9.87984E-01  9.88306E-01  9.91001E-01  9.87829E-01  9.90047E-01  9.97776E-01  9.89776E-01  1.00670E+00  9.91110E-01  9.90585E-01  9.98066E-01  1.00112E+00  1.00003E+00  9.82402E-01  9.93692E-01  9.89993E-01  ];
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
TOT_COL_EFF               (idx, [1:   4]) = [  9.80576E-01 9.5E-07  0.00000E+00 0.0E+00 ];
TMS_MAJORANT_FAIL         (idx, 1)        =  0.00000E+00 ;
TMS_LIMITS_FAIL           (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
AVG_TRACKS                (idx, [1:   4]) = [  8.55324E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_REAL_COL              (idx, [1:   4]) = [  8.55226E+01 0.00021  0.00000E+00 0.0E+00 ];
AVG_VIRT_COL              (idx, [1:   4]) = [  1.69416E+00 0.00023  0.00000E+00 0.0E+00 ];
AVG_SURF_CROSS            (idx, [1:   4]) = [  1.27640E+02 0.00024  0.00000E+00 0.0E+00 ];

% Run statistics:

CYCLE_IDX                 (idx, 1)        = 6000 ;
SOURCE_NEUTRONS           (idx, 1)        = 2107518885 ;
MEAN_POP_SIZE             (idx, [1:  2])  = [  3.51253E+05 0.00050 ];
MEAN_POP_WGT              (idx, [1:  2])  = [  3.00005E+04 0.00008 ];
SIMULATION_COMPLETED      (idx, 1)        = 1 ;

% Running times:

TOT_CPU_TIME              (idx, 1)        =  3.43359E+04 ;
RUNNING_TIME              (idx, 1)        =  1.18981E+03 ;
INIT_TIME                 (idx, [1:  2])  = [  3.73567E-01  3.73567E-01 ];
PROCESS_TIME              (idx, [1:  2])  = [  9.38333E-03  9.38333E-03 ];
TRANSPORT_CYCLE_TIME      (idx, [1:  3])  = [  1.18943E+03  1.18943E+03  0.00000E+00 ];
BURNUP_CYCLE_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
BATEMAN_SOLUTION_TIME     (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
MPI_OVERHEAD_TIME         (idx, [1:  2])  = [  0.00000E+00  0.00000E+00 ];
ESTIMATED_RUNNING_TIME    (idx, [1:  2])  = [  1.18981E+03  0.00000E+00 ];
CPU_USAGE                 (idx, 1)        = 28.85818 ;
TRANSPORT_CPU_USAGE       (idx, [1:   2]) = [  2.88659E+01 3.0E-05 ];
OMP_PARALLEL_FRAC         (idx, 1)        =  9.85773E-01 ;
OMP_AMDAHL_MAX            (idx, 1)        = 21.24 ;

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

NORM_COEF                 (idx, [1:   4]) = [  3.32887E-05 3.4E-05  0.00000E+00 0.0E+00 ];

% Analog reaction rate estimators:

CONVERSION_RATIO          (idx, [1:   2]) = [  5.10179E-01 9.8E-05 ];
U235_FISS_FRAC            (idx, [1:   2]) = [  9.38076E-01 1.6E-05 ];
U238_FISS_FRAC            (idx, [1:   2]) = [  6.19243E-02 0.00025 ];

% Normalized total reaction rates (neutrons):

TOT_POWER                 (idx, [1:   2]) = [  1.32438E-11 3.1E-05 ];
TOT_POWDENS               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_GENRATE               (idx, [1:   2]) = [  9.98505E-01 3.1E-05 ];
TOT_FISSRATE              (idx, [1:   2]) = [  4.08727E-01 3.1E-05 ];
TOT_CAPTRATE              (idx, [1:   2]) = [  5.73541E-01 2.3E-05 ];
TOT_ABSRATE               (idx, [1:   2]) = [  9.82268E-01 9.2E-06 ];
TOT_SRCRATE               (idx, [1:   2]) = [  9.98662E-01 3.4E-05 ];
TOT_FLUX                  (idx, [1:   2]) = [  4.34502E+01 3.0E-05 ];
TOT_LEAKRATE              (idx, [1:   2]) = [  1.77315E-02 0.00051 ];
ALBEDO_LEAKRATE           (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_LOSSRATE              (idx, [1:   2]) = [  1.00000E+00 0.0E+00 ];
TOT_CUTRATE               (idx, [1:   2]) = [  0.00000E+00 0.0E+00 ];
TOT_RR                    (idx, [1:   2]) = [  6.06221E+01 4.9E-05 ];
INI_FMASS                 (idx, 1)        =  0.00000E+00 ;
TOT_FMASS                 (idx, 1)        =  0.00000E+00 ;

% Fission neutron and energy production:

NUBAR                     (idx, [1:   2]) = [  2.44296E+00 1.1E-06 ];
FISSE                     (idx, [1:   2]) = [  2.02241E+02 1.4E-07 ];

% Criticality eigenvalues:

ANA_KEFF                  (idx, [1:   6]) = [  9.99790E-01 5.3E-05  9.92273E-01 5.0E-05  7.52195E-03 0.00072 ];
IMP_KEFF                  (idx, [1:   2]) = [  9.99804E-01 3.1E-05 ];
COL_KEFF                  (idx, [1:   2]) = [  9.99850E-01 4.5E-05 ];
ABS_KEFF                  (idx, [1:   2]) = [  9.99804E-01 3.1E-05 ];
ABS_KINF                  (idx, [1:   2]) = [  1.01788E+00 2.9E-05 ];
GEOM_ALBEDO               (idx, [1:   6]) = [  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00  1.00000E+00 0.0E+00 ];

% Forward-weighted delayed neutron parameters:

FWD_ANA_BETA_ZERO         (idx, [1:  18]) = [  1.97119E-03 0.00190  5.64793E-05 0.00922  2.85040E-04 0.00426  1.61589E-04 0.00527  3.67062E-04 0.00355  6.35435E-04 0.00299  2.16719E-04 0.00489  1.77663E-04 0.00550  7.12037E-05 0.00922 ];
FWD_ANA_LAMBDA            (idx, [1:  18]) = [  4.61956E-01 0.00074  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Beta-eff using Meulekamp's method:

ADJ_MEULEKAMP_BETA_EFF    (idx, [1:  18]) = [  7.58113E-03 0.00069  2.26930E-04 0.00400  1.09364E-03 0.00177  6.43059E-04 0.00236  1.42793E-03 0.00157  2.45007E-03 0.00119  8.11443E-04 0.00212  6.73500E-04 0.00226  2.54564E-04 0.00371 ];
ADJ_MEULEKAMP_LAMBDA      (idx, [1:  18]) = [  4.63550E-01 0.00106  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using Nauchi's method:

ADJ_NAUCHI_GEN_TIME       (idx, [1:   6]) = [  4.78626E-05 0.00011  4.78408E-05 0.00011  5.07089E-05 0.00095 ];
ADJ_NAUCHI_LIFETIME       (idx, [1:   6]) = [  4.78517E-05 9.1E-05  4.78299E-05 9.1E-05  5.06972E-05 0.00095 ];
ADJ_NAUCHI_BETA_EFF       (idx, [1:  18]) = [  7.52407E-03 0.00074  2.24972E-04 0.00421  1.08661E-03 0.00192  6.38299E-04 0.00251  1.41535E-03 0.00172  2.43400E-03 0.00128  8.03709E-04 0.00227  6.69279E-04 0.00247  2.51849E-04 0.00410 ];
ADJ_NAUCHI_LAMBDA         (idx, [1:  18]) = [  4.63272E-01 0.00116  1.24667E-02 4.5E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];

% Adjoint weighted time constants using IFP:

ADJ_IFP_GEN_TIME          (idx, [1:   6]) = [  4.71185E-05 0.00021  4.70974E-05 0.00021  4.98942E-05 0.00221 ];
ADJ_IFP_LIFETIME          (idx, [1:   6]) = [  4.71079E-05 0.00021  4.70868E-05 0.00021  4.98826E-05 0.00220 ];
ADJ_IFP_IMP_BETA_EFF      (idx, [1:  18]) = [  7.65498E-03 0.00213  2.33251E-04 0.01215  1.10496E-03 0.00567  6.53893E-04 0.00726  1.44196E-03 0.00496  2.47699E-03 0.00372  8.10828E-04 0.00652  6.81883E-04 0.00726  2.51224E-04 0.01165 ];
ADJ_IFP_IMP_LAMBDA        (idx, [1:  18]) = [  4.60500E-01 0.00328  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ANA_BETA_EFF      (idx, [1:  18]) = [  7.65179E-03 0.00208  2.33782E-04 0.01191  1.10423E-03 0.00556  6.54340E-04 0.00714  1.43948E-03 0.00483  2.47641E-03 0.00365  8.10916E-04 0.00637  6.80775E-04 0.00712  2.51866E-04 0.01137 ];
ADJ_IFP_ANA_LAMBDA        (idx, [1:  18]) = [  4.60592E-01 0.00322  1.24667E-02 5.0E-09  2.82917E-02 0.0E+00  4.25244E-02 6.8E-09  1.33042E-01 0.0E+00  2.92467E-01 4.4E-09  6.66488E-01 6.7E-09  1.63478E+00 3.3E-09  3.55460E+00 6.9E-09 ];
ADJ_IFP_ROSSI_ALPHA       (idx, [1:   2]) = [ -1.62579E+02 0.00214 ];

% Adjoint weighted time constants using perturbation technique:

ADJ_PERT_GEN_TIME         (idx, [1:   2]) = [  4.74870E-05 6.6E-05 ];
ADJ_PERT_LIFETIME         (idx, [1:   2]) = [  4.74762E-05 4.0E-05 ];
ADJ_PERT_BETA_EFF         (idx, [1:   2]) = [  7.63677E-03 0.00042 ];
ADJ_PERT_ROSSI_ALPHA      (idx, [1:   2]) = [ -1.60823E+02 0.00043 ];

% Inverse neutron speed :

ANA_INV_SPD               (idx, [1:   2]) = [  1.36824E-06 5.2E-05 ];

% Analog slowing-down and thermal neutron lifetime (total/prompt/delayed):

ANA_SLOW_TIME             (idx, [1:   6]) = [  1.96617E-06 4.8E-05  1.96601E-06 4.8E-05  1.98731E-06 0.00056 ];
ANA_THERM_TIME            (idx, [1:   6]) = [  7.20002E-05 7.4E-05  7.20593E-05 7.4E-05  6.42503E-05 0.00084 ];
ANA_THERM_FRAC            (idx, [1:   6]) = [  8.02889E-01 2.1E-05 -3.50466E-02 0.00175  2.56368E-04 0.00177 ];
ANA_DELAYED_EMTIME        (idx, [1:   2]) = [  1.21657E+01 0.00108 ];

% Group constant generation:

GC_UNIVERSE_NAME          (idx, [1:  1])  = '0' ;

% Micro- and macro-group structures:

MICRO_NG                  (idx, 1)        = 70 ;
MICRO_E                   (idx, [1:  71]) = [  2.00000E+01  6.06550E+00  3.67900E+00  2.23100E+00  1.35300E+00  8.21000E-01  5.00000E-01  3.02500E-01  1.83000E-01  1.11000E-01  6.74300E-02  4.08500E-02  2.47800E-02  1.50300E-02  9.11800E-03  5.50000E-03  3.51910E-03  2.23945E-03  1.42510E-03  9.06898E-04  3.67262E-04  1.48728E-04  7.55014E-05  4.80520E-05  2.77000E-05  1.59680E-05  9.87700E-06  4.00000E-06  3.30000E-06  2.60000E-06  2.10000E-06  1.85500E-06  1.50000E-06  1.30000E-06  1.15000E-06  1.12300E-06  1.09700E-06  1.07100E-06  1.04500E-06  1.02000E-06  9.96000E-07  9.72000E-07  9.50000E-07  9.10000E-07  8.50000E-07  7.80000E-07  6.25000E-07  5.00000E-07  4.00000E-07  3.50000E-07  3.20000E-07  3.00000E-07  2.80000E-07  2.50000E-07  2.20000E-07  1.80000E-07  1.40000E-07  1.00000E-07  8.00000E-08  6.70000E-08  5.80000E-08  5.00000E-08  4.20000E-08  3.50000E-08  3.00000E-08  2.50000E-08  2.00000E-08  1.50000E-08  1.00000E-08  5.00000E-09  1.00000E-11 ];

MACRO_NG                  (idx, 1)        = 2 ;
MACRO_E                   (idx, [1:   3]) = [  1.00000E+37  6.25000E-07  0.00000E+00 ];

% Integral parameters:

INF_KINF                  (idx, [1:   2]) = [  1.01796E+00 5.4E-05 ];

% Flux spectrum in infinite geometry:

INF_FLX                   (idx, [1:   4]) = [  2.73313E+01 4.3E-05  1.61190E+01 6.5E-05 ];

% Reaction cross sections:

INF_TOT                   (idx, [1:   4]) = [  6.94160E-01 2.8E-05  2.58391E+00 2.9E-05 ];
INF_CAPT                  (idx, [1:   4]) = [  4.94208E-03 7.8E-05  2.72022E-02 3.3E-05 ];
INF_ABS                   (idx, [1:   4]) = [  6.69156E-03 6.3E-05  4.95928E-02 5.9E-05 ];
INF_FISS                  (idx, [1:   4]) = [  1.74948E-03 5.7E-05  2.23906E-02 9.5E-05 ];
INF_NSF                   (idx, [1:   4]) = [  4.53699E-03 5.9E-05  5.42534E-02 9.5E-05 ];
INF_NUBAR                 (idx, [1:   4]) = [  2.59333E+00 7.3E-06  2.42304E+00 0.0E+00 ];
INF_KAPPA                 (idx, [1:   4]) = [  2.04500E+02 6.6E-07  2.01942E+02 8.1E-09 ];
INF_INVV                  (idx, [1:   4]) = [  6.31287E-08 5.4E-05  3.58121E-06 1.5E-05 ];

% Total scattering cross sections:

INF_SCATT0                (idx, [1:   4]) = [  6.87461E-01 2.8E-05  2.53432E+00 3.0E-05 ];
INF_SCATT1                (idx, [1:   4]) = [  3.48017E-01 3.2E-05  5.21841E-01 3.2E-05 ];
INF_SCATT2                (idx, [1:   4]) = [  1.36039E-01 3.8E-05  8.99205E-02 8.6E-05 ];
INF_SCATT3                (idx, [1:   4]) = [  9.07201E-03 0.00031  2.38134E-02 0.00026 ];
INF_SCATT4                (idx, [1:   4]) = [ -1.58440E-02 0.00016 -2.04756E-02 0.00030 ];
INF_SCATT5                (idx, [1:   4]) = [  6.52045E-05 0.03191  1.14242E-02 0.00047 ];
INF_SCATT6                (idx, [1:   4]) = [  7.19729E-03 0.00027 -3.10596E-02 0.00017 ];
INF_SCATT7                (idx, [1:   4]) = [  8.11186E-04 0.00228  1.06828E-02 0.00039 ];

% Total scattering production cross sections:

INF_SCATTP0               (idx, [1:   4]) = [  6.87518E-01 2.8E-05  2.53432E+00 3.0E-05 ];
INF_SCATTP1               (idx, [1:   4]) = [  3.48019E-01 3.2E-05  5.21841E-01 3.2E-05 ];
INF_SCATTP2               (idx, [1:   4]) = [  1.36041E-01 3.8E-05  8.99205E-02 8.6E-05 ];
INF_SCATTP3               (idx, [1:   4]) = [  9.07218E-03 0.00031  2.38134E-02 0.00026 ];
INF_SCATTP4               (idx, [1:   4]) = [ -1.58440E-02 0.00016 -2.04756E-02 0.00030 ];
INF_SCATTP5               (idx, [1:   4]) = [  6.52219E-05 0.03189  1.14242E-02 0.00047 ];
INF_SCATTP6               (idx, [1:   4]) = [  7.19731E-03 0.00027 -3.10596E-02 0.00017 ];
INF_SCATTP7               (idx, [1:   4]) = [  8.11211E-04 0.00228  1.06828E-02 0.00039 ];

% Diffusion parameters:

INF_TRANSPXS              (idx, [1:   4]) = [  2.44592E-01 3.7E-05  1.73445E+00 3.8E-05 ];
INF_DIFFCOEF              (idx, [1:   4]) = [  1.36282E+00 3.7E-05  1.92184E-01 3.8E-05 ];

% Reduced absoption and removal:

INF_RABSXS                (idx, [1:   4]) = [  6.63490E-03 6.3E-05  4.95921E-02 5.9E-05 ];
INF_REMXS                 (idx, [1:   4]) = [  3.61687E-02 4.1E-05  4.98204E-02 7.3E-05 ];

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

INF_CHIT                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  1.07676E-09 0.56546 ];
INF_CHIP                  (idx, [1:   4]) = [  1.00000E+00 0.0E+00  1.05917E-10 1.00000 ];
INF_CHID                  (idx, [1:   4]) = [  1.00000E+00 8.1E-08  1.31049E-07 0.62114 ];

% Scattering matrixes:

INF_S0                    (idx, [1:   8]) = [  6.57992E-01 2.8E-05  2.94693E-02 3.9E-05  2.29917E-04 0.00070  2.53409E+00 3.0E-05 ];
INF_S1                    (idx, [1:   8]) = [  3.39377E-01 3.2E-05  8.63938E-03 7.2E-05  1.32000E-04 0.00090  5.21709E-01 3.2E-05 ];
INF_S2                    (idx, [1:   8]) = [  1.39053E-01 3.7E-05 -3.01383E-03 0.00017  8.32407E-05 0.00104  8.98373E-02 8.6E-05 ];
INF_S3                    (idx, [1:   8]) = [  1.24348E-02 0.00023 -3.36278E-03 0.00013  4.27973E-05 0.00157  2.37706E-02 0.00026 ];
INF_S4                    (idx, [1:   8]) = [ -1.50551E-02 0.00016 -7.88887E-04 0.00049  1.37531E-05 0.00423 -2.04893E-02 0.00030 ];
INF_S5                    (idx, [1:   8]) = [ -2.65034E-04 0.00767  3.30239E-04 0.00100 -2.54654E-06 0.02078  1.14267E-02 0.00047 ];
INF_S6                    (idx, [1:   8]) = [  7.46024E-03 0.00026 -2.62950E-04 0.00116 -9.49136E-06 0.00479 -3.10501E-02 0.00017 ];
INF_S7                    (idx, [1:   8]) = [  1.27504E-03 0.00143 -4.63852E-04 0.00066 -1.13480E-05 0.00397  1.06941E-02 0.00039 ];

% Scattering production matrixes:

INF_SP0                   (idx, [1:   8]) = [  6.58048E-01 2.8E-05  2.94693E-02 3.9E-05  2.29917E-04 0.00070  2.53409E+00 3.0E-05 ];
INF_SP1                   (idx, [1:   8]) = [  3.39380E-01 3.2E-05  8.63938E-03 7.2E-05  1.32000E-04 0.00090  5.21709E-01 3.2E-05 ];
INF_SP2                   (idx, [1:   8]) = [  1.39055E-01 3.7E-05 -3.01383E-03 0.00017  8.32407E-05 0.00104  8.98373E-02 8.6E-05 ];
INF_SP3                   (idx, [1:   8]) = [  1.24350E-02 0.00023 -3.36278E-03 0.00013  4.27973E-05 0.00157  2.37707E-02 0.00026 ];
INF_SP4                   (idx, [1:   8]) = [ -1.50551E-02 0.00016 -7.88888E-04 0.00049  1.37531E-05 0.00423 -2.04893E-02 0.00030 ];
INF_SP5                   (idx, [1:   8]) = [ -2.65017E-04 0.00767  3.30239E-04 0.00100 -2.54655E-06 0.02078  1.14267E-02 0.00047 ];
INF_SP6                   (idx, [1:   8]) = [  7.46026E-03 0.00026 -2.62950E-04 0.00116 -9.49136E-06 0.00479 -3.10501E-02 0.00017 ];
INF_SP7                   (idx, [1:   8]) = [  1.27506E-03 0.00143 -4.63852E-04 0.00066 -1.13480E-05 0.00397  1.06941E-02 0.00039 ];

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

