package None;

/* metamodel_version: 1.7.0 */
/* version: 1.2.1 */
import java.util.List;
import lombok.*;

/**
  Used to indicate that a task is dependent on another task.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class TaskDependency  {

  private String task-uuid;
  private String remarks;

}