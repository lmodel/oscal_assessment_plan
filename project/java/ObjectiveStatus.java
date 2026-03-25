package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A determination of if the objective is satisfied or not within a given system.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class ObjectiveStatus  {

  private String state;
  private String reason;
  private String remarks;

}