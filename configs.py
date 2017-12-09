# Copyright 2017 The TensorFlow Agents Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Example configurations using the PPO algorithm."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

# pylint: disable=unused-variable

from agents import AOCAgent
from agents import ACAgent
from agents import TabSFAgent
from agents import ACSFAgent
from agents import ACOptionAgent
from agents import ACMatrixAgent
from agents import LinearSFAgent
from agents import DIFAgent
from agents import SFAgent
from env_wrappers import GridWorld
from env_wrappers import Gridworld_NonMatching
import functools
import networks


def default():
  """Default configuration for PPO."""
  num_agents = 8
  eval_episodes = 1
  use_gpu = False
  max_length = 100
  return locals()

def aoc():
  locals().update(default())
  agent = AOCAgent
  num_agents = 8
  use_gpu = False

  # Network
  network = networks.AOCNetwork
  weight_summaries = dict(
      all=r'.*',
      conv=r'.*/conv/.*',
      fc=r'.*/fc/.*',
      term=r'.*/option_term/.*',
      q_val=r'.*/q_val/.*',
      policy=r'.*/i_o_policies/.*')

  # conv_layers = (8, 4, 16), (4, 2, 32)
  input_size = (13,13)
  history_size = 3
  conv_layers = (5, 2, 32),
  deconv_layers = (4, 2, 0, 128), (4, 2, 1, 64), (4, 2, 0, 32), ()
  # fc_layers = 256,
  fc_layers = 128,
  sf_layers = 256, 128, 256
  # Optimization
  network_optimizer = 'AdamOptimizer'
  # lr = 0.0007
  lr = 1e-3

  # Losses
  discount = 0.985

  entropy_coef = 1e-4 #0.01
  critic_coef = 0.5

  # nb_options = 8
  nb_options = 4
  env = functools.partial(
    GridWorld, "./mdps/4rooms.mdp")
  # env = Gridworld_NonMatching
  max_update_freq = 30
  min_update_freq = 5
  steps = 1e6  # 1M
  explore_steps = 1
  final_random_action_prob = 0.1
  initial_random_action_prob = 1.0
  delib_cost = 0
  margin_cost = 0
  gradient_clip_value = 40
  summary_interval = 1
  checkpoint_interval = 1
  eval_interval = 100

  return locals()

def sf():
  locals().update(default())
  agent = SFAgent
  num_agents = 8
  use_gpu = False

  # Network
  network = networks.SFNetwork
  weight_summaries = dict(
      all=r'.*',
      conv=r'.*/conv/.*',
      fc=r'.*/fc/.*',
      term=r'.*/option_term/.*',
      q_val=r'.*/q_val/.*',
      policy=r'.*/i_o_policies/.*')

  # conv_layers = (8, 4, 16), (4, 2, 32)
  input_size = (16, 16)
  history_size = 3
  conv_layers = (5, 2, 32),
  deconv_layers = (4, 2, 0, 128), (4, 2, 1, 64), (2, 2, 0, 3)
  # fc_layers = 256,
  fc_layers = 128,
  sf_layers = 256, 128
  # Optimization
  network_optimizer = 'AdamOptimizer'
  # lr = 0.0007
  lr = 1e-3

  # Losses
  discount = 0.985

  entropy_coef = 1e-4 #0.01
  # critic_coef = 0.5
  sf_coef = 0.5
  instant_r_coef = 0.5
  auto_coef = 1

  # nb_options = 8
  nb_options = 4
  env = functools.partial(
    GridWorld, "./mdps/toy.mdp")
  # env = Gridworld_NonMatching
  max_update_freq = 30
  min_update_freq = 5
  steps = 1e6  # 1M
  explore_steps = 1
  final_random_action_prob = 0.1
  initial_random_action_prob = 1.0
  delib_cost = 0
  margin_cost = 0
  gradient_clip_value = 40
  summary_interval = 1
  checkpoint_interval = 1
  eval_interval = 100

  return locals()

def ac():
  locals().update(default())
  policy_agent = ACAgent
  sf_agent = ACSFAgent
  option_agent = ACOptionAgent
  matrix_agent = ACMatrixAgent
  tabular_sf_agent = TabSFAgent
  linear_sf_agent = LinearSFAgent
  num_agents = 8
  use_gpu = False
  nb_options = 4
  # Network
  network = networks.ACNetwork
  weight_summaries = dict(
      all=r'.*',
      conv=r'.*/conv/.*',
      fc=r'.*/fc/.*',
      term=r'.*/option_term/.*',
      q_val=r'.*/q_val/.*',
      policy=r'.*/i_o_policies/.*')

  # conv_layers = (8, 4, 16), (4, 2, 32)
  input_size = (7, 6)
  history_size = 3
  conv_layers = (5, 2, 32),
  fc_layers = 128,
  sf_layers = 128, 128
  # Optimization
  network_optimizer = 'AdamOptimizer'
  # lr = 0.0007
  lr = 1e-3
  sf_lr = 1e-3
  discount = 0.985
  entropy_coef = 1e-4 #0.01
  critic_coef = 0.5
  sf_coef = 1
  instant_r_coef = 1
  option_entropy_coef = 0.01
  auto_coef = 1

  env = functools.partial(
    GridWorld, "./mdps/2rooms.mdp")
  max_update_freq = 30
  min_update_freq = 5
  steps = 1e6  # 1M
  explore_steps = 1e5
  final_random_action_prob = 0.1
  initial_random_action_prob = 1.0
  delib_cost = 0
  margin_cost = 0
  gradient_clip_value = 40
  summary_interval = 10
  checkpoint_interval = 1
  eval_interval = 1
  policy_steps = 1e3
  sf_transition_matrix_steps = 300#e3
  sf_transition_options_steps = 400#e3
  sf_transition_matrix_size = 1e3

  return locals()

def linear():
  locals().update(default())
  linear_sf_agent = LinearSFAgent
  num_agents = 8
  use_gpu = False
  nb_options = 4
  # Network
  network = networks.LinearSFNetwork
  weight_summaries = dict(
      all=r'.*',
      conv=r'.*/conv/.*',
      fc=r'.*/fc/.*',
      term=r'.*/option_term/.*',
      q_val=r'.*/q_val/.*',
      policy=r'.*/i_o_policies/.*')

  # conv_layers = (8, 4, 16), (4, 2, 32)
  input_size = (7, 6)
  history_size = 3
  conv_layers = (5, 2, 32),
  fc_layers = 128,
  sf_layers = 128, 128
  # Optimization
  network_optimizer = 'AdamOptimizer'
  # lr = 0.0007
  lr = 1e-3
  sf_lr = 1e-3
  discount = 0.985
  entropy_coef = 1e-4 #0.01
  critic_coef = 0.5
  sf_coef = 1
  instant_r_coef = 1
  option_entropy_coef = 0.01
  auto_coef = 1

  env = functools.partial(
    GridWorld, "./mdps/2rooms.mdp")
  max_update_freq = 30
  min_update_freq = 5
  steps = 1e6  # 1M
  explore_steps = 1e5
  final_random_action_prob = 0.1
  initial_random_action_prob = 1.0
  delib_cost = 0
  margin_cost = 0
  gradient_clip_value = 40
  summary_interval = 10
  checkpoint_interval = 1
  eval_interval = 1
  policy_steps = 1e3
  sf_transition_matrix_steps = 300#e3
  sf_transition_options_steps = 400#e3
  sf_transition_matrix_size = 1e3

  return locals()

def linear_4rooms():
  locals().update(default())
  linear_sf_agent = LinearSFAgent
  num_agents = 8
  use_gpu = False
  nb_options = 4
  # Network
  network = networks.LinearSFNetwork
  weight_summaries = dict(
      all=r'.*',
      conv=r'.*/conv/.*',
      fc=r'.*/fc/.*',
      term=r'.*/option_term/.*',
      q_val=r'.*/q_val/.*',
      policy=r'.*/i_o_policies/.*')

  # conv_layers = (8, 4, 16), (4, 2, 32)
  input_size = (13, 13)
  history_size = 3
  conv_layers = (5, 2, 32),
  fc_layers = 128,
  sf_layers = 128, 128
  # Optimization
  network_optimizer = 'AdamOptimizer'
  # lr = 0.0007
  lr = 1e-3
  sf_lr = 1e-3
  discount = 0.985
  entropy_coef = 1e-4 #0.01
  critic_coef = 0.5
  sf_coef = 1
  instant_r_coef = 1
  option_entropy_coef = 0.01
  auto_coef = 1

  env = functools.partial(
    GridWorld, "./mdps/4rooms.mdp")
  max_update_freq = 30
  min_update_freq = 5
  steps = 1e6  # 1M
  explore_steps = 1e5
  final_random_action_prob = 0.1
  initial_random_action_prob = 1.0
  delib_cost = 0
  margin_cost = 0
  gradient_clip_value = 40
  summary_interval = 10
  checkpoint_interval = 1
  eval_interval = 1
  policy_steps = 1e3
  sf_transition_matrix_steps = 300#e3
  sf_transition_options_steps = 400#e3
  sf_transition_matrix_size = 1e3

  return locals()


def dif_4rooms():
  locals().update(default())
  dif_agent = DIFAgent
  num_agents = 8
  use_gpu = False
  nb_options = 4
  # Network
  network = networks.DIFNetwork
  weight_summaries = dict(
      all=r'.*',
      conv=r'.*/conv/.*',
      fc=r'.*/fc/.*',
      term=r'.*/option_term/.*',
      q_val=r'.*/q_val/.*',
      policy=r'.*/i_o_policies/.*')

  conv_layers = (5, 2, 64),
  input_size = (13, 13)
  history_size = 3
  fc_layers = 128,
  sf_layers = 128, 256, 128
  aux_fc_layers = 128,
  aux_deconv_layers = (5, 1, 0, 13*13*3), #(4, 2, 1, 64), (4, 2, 1, 64), (4, 2, 1, 64), (6, 1, 0, 3)
  # Optimization
  network_optimizer = 'RMSPropOptimizer'
  # lr = 0.0007
  lr = 1e-4
  discount = 0.985
  entropy_coef = 1e-4
  critic_coef = 0.5
  sf_coef = 1
  instant_r_coef = 1
  option_entropy_coef = 0.01
  aux_coef = 1

  env = functools.partial(
    GridWorld, "./mdps/4rooms.mdp")
  max_update_freq = 30
  min_update_freq = 5
  steps = 1e6   # 1M
  training_steps = 5e5
  explore_steps = 1e5
  final_random_action_prob = 0.1
  initial_random_action_prob = 1.0
  delib_cost = 0
  margin_cost = 0
  gradient_clip_value = 40
  summary_interval = 10
  checkpoint_interval = 10
  eval_interval = 1
  policy_steps = 1e3
  # sf_transition_matrix_steps = 50000#e3
  # sf_transition_options_steps = 50000#e3
  sf_transition_matrix_size = 50000

  return locals()