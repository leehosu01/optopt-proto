
import tempfile
from tf_agents.environments import py_environment

class Management_class:
    def __init__(self):
        pass
class Environment_class(py_environment.PyEnvironment):
    def __init__(self):
        pass
class Agency_class:
    def __init__(self):
        pass
class Variable_class:
    def __init__(self):
        pass
    def get_param_names(self): return self.hyper_parameters_names
    def get_param_cnt(self):   return len(self.hyper_parameters)
class Config:
    def __init__(self, 
                lstm_size = [256],
                replay_buffer_capacity = 10000,
                sequence_length = 5,
                train_batch_size = 32,
                train_iterations = 1,
                parallel_env_cnt = None,
                critic_learning_rate = 3e-4,
                actor_learning_rate = 3e-4,
                alpha_learning_rate = 3e-4,
                target_update_tau = 0.005,
                target_update_period = 1,
                gamma = 1.00 ,
                log_interval = 1,
                collect_episodes_for_training = 1,
                collect_episodes_for_env_testing = 0,
                policy_save_interval = 4,
                savedir = tempfile.gettempdir(),
                dtype = 'float32',
                verbose = 0):
        assert parallel_env_cnt == None# still not implemented!
        self.lstm_size = lstm_size
        self.replay_buffer_capacity = replay_buffer_capacity
        self.sequence_length = sequence_length
        self.train_batch_size = train_batch_size
        self.train_iterations = train_iterations
        self.parallel_env_cnt = parallel_env_cnt
        self.critic_learning_rate =critic_learning_rate
        self.actor_learning_rate = actor_learning_rate
        self.alpha_learning_rate = alpha_learning_rate
        self.target_update_tau = target_update_tau
        self.target_update_period = target_update_period
        self.gamma = gamma 
        self.log_interval = log_interval
        self.collect_episodes_for_training = collect_episodes_for_training
        self.collect_episodes_for_env_testing = collect_episodes_for_env_testing
        self.policy_save_interval = policy_save_interval
        self.savedir = savedir
        self.dtype = dtype
        self.verbose = verbose
